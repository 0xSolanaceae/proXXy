import asyncio
import json
import logging
import os
import re
from functools import lru_cache
from typing import Dict, Iterable, List, Set, Tuple

import aiohttp
from tqdm import tqdm

PROXY_PATTERN = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}:\d{2,5}\b")


def load_proxy_sources(file_path: str = "proxy_sources.json") -> Dict[str, List[str]]:
    """Load proxy source URLs grouped by protocol from disk."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


@lru_cache(maxsize=1)
def proxy_sources() -> Dict[str, List[str]]:
    """Cached read of proxy sources; they rarely change during one run."""
    return load_proxy_sources()


def parse_proxies(blob: str) -> List[str]:
    """Extract host:port pairs from raw text."""
    return PROXY_PATTERN.findall(blob)


def dedupe_preserve_order(items: Iterable[str]) -> List[str]:
    seen: Set[str] = set()
    out: List[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def read_proxy_file(path: str) -> List[str]:
    if not os.path.isfile(path):
        return []
    with open(path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def write_proxy_file(path: str, proxies: Iterable[str]):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        for proxy in proxies:
            file.write(f"{proxy}\n")


async def _fetch_source(session: aiohttp.ClientSession, url: str, timeout: int, retries: int, backoff: float) -> str:
    """Fetch a proxy source with retries; returns raw body or empty string."""
    for attempt in range(retries + 1):
        try:
            async with session.get(url, timeout=timeout) as resp:
                resp.raise_for_status()
                return await resp.text(errors="ignore")
        except Exception as exc:  # noqa: BLE001 (broad to log and continue)
            logging.warning("Source fetch failed (%s/%s): %s", attempt + 1, retries + 1, url)
            if attempt == retries:
                logging.error("Giving up on %s: %s", url, exc)
                return ""
            await asyncio.sleep(backoff * (attempt + 1))
    return ""


async def scrape_sources_async(
    sources: Dict[str, List[str]],
    *,
    concurrency: int = 100,
    timeout: int = 8,
    retries: int = 2,
    backoff: float = 0.5,
) -> Dict[str, List[str]]:
    """Fetch all sources concurrently and return proxies grouped by protocol."""
    connector = aiohttp.TCPConnector(limit=concurrency)
    timeout_cfg = aiohttp.ClientTimeout(total=timeout)
    sem = asyncio.Semaphore(concurrency)
    results: Dict[str, List[str]] = {key: [] for key in sources.keys()}

    async with aiohttp.ClientSession(connector=connector, timeout=timeout_cfg) as session:
        tasks = []
        for protocol, urls in sources.items():
            for url in urls:
                async def task(proto=protocol, src=url):
                    async with sem:
                        body = await _fetch_source(session, src, timeout, retries, backoff)
                        if not body:
                            return proto, []
                        return proto, parse_proxies(body)
                tasks.append(task())

        for coro in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Scraping sources", unit="src", ascii=True):
            protocol, proxies = await coro
            results.setdefault(protocol, []).extend(proxies)

    for protocol, proxies in results.items():
        results[protocol] = dedupe_preserve_order(proxies)
    return results


async def _check_proxies_async(
    proxies: List[str],
    *,
    test_url: str,
    proxy_scheme: str,
    concurrency: int = 200,
    timeout: int = 5,
    limit: int | None = None,
) -> List[str]:
    connector = aiohttp.TCPConnector(limit=0)
    timeout_cfg = aiohttp.ClientTimeout(total=timeout)
    sem = asyncio.Semaphore(concurrency)
    valid: List[str] = []

    async with aiohttp.ClientSession(connector=connector, timeout=timeout_cfg) as session:
        async def check(proxy: str):
            proxy_url = f"{proxy_scheme}://{proxy}"
            async with sem:
                try:
                    async with session.get(test_url, proxy=proxy_url) as resp:
                        if 100 <= resp.status < 400:
                            return proxy
                except Exception:
                    return None
            return None

        tasks = [asyncio.create_task(check(p)) for p in proxies]

        for coro in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc=f"Validating {proxy_scheme.upper()}", unit="prox", ascii=True):
            result = await coro
            if result:
                valid.append(result)

            if limit and len(valid) >= limit:
                for pending in tasks:
                    if not pending.done():
                        pending.cancel()
                await asyncio.gather(*tasks, return_exceptions=True)
                break

    return valid


def validate_proxy_file(
    file_path: str,
    *,
    test_url: str,
    proxy_scheme: str,
    concurrency: int = 200,
    timeout: int = 5,
    limit: int | None = None,
):
    proxies = read_proxy_file(file_path)
    if not proxies:
        print(f"No proxies found in {file_path}")
        return

    import time
    start = time.perf_counter()
    valid = asyncio.run(
        _check_proxies_async(
            proxies,
            test_url=test_url,
            proxy_scheme=proxy_scheme,
            concurrency=concurrency,
            timeout=timeout,
            limit=limit,
        )
    )
    elapsed = time.perf_counter() - start

    print(f"[*] Valid {proxy_scheme.upper()} proxies: {len(valid):,}")
    print(f"[*] Validation time: {elapsed:.2f}s")

    capped = valid if not limit else valid[:limit]
    write_proxy_file(file_path, dedupe_preserve_order(capped))


def http_check(file_path: str, *, concurrency: int = 400, timeout: int = 3, limit: int | None = None):
    validate_proxy_file(
        file_path,
        test_url="http://httpbin.org/ip",
        proxy_scheme="http",
        concurrency=concurrency,
        timeout=timeout,
        limit=limit,
    )


def https_check(file_path: str, *, concurrency: int = 400, timeout: int = 3, limit: int | None = None):
    validate_proxy_file(
        file_path,
        test_url="https://api.myip.com/",
        proxy_scheme="http",
        concurrency=concurrency,
        timeout=timeout,
        limit=limit,
    )
