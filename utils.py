import contextlib
import os
import json
import time
import logging
import requests
from tqdm import tqdm
from yaspin import yaspin
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List


def load_proxy_sources(file_path: str) -> Dict[str, List[str]]:
    """Load proxy source URLs grouped by protocol from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)


def proxy_sources() -> Dict[str, List[str]]:
    """Return proxy source URLs from the default JSON file in the repo."""
    return load_proxy_sources('proxy_sources.json')


def http_check(PROXY_LIST_FILE: str): 
    # combine two methods into one, so that when it's called it'll differentiate based upon what type of proxy parameter is fed into it
    TEST_URL = "http://httpbin.org/ip"  # https://httpbin.org/anything # https://api.myip.com/ #FIXME add in time to reach judge sites in milliseconds
    TIMEOUT = 5
    # Ensure logs are written under output/
    os.makedirs('output', exist_ok=True)
    logging.basicConfig(filename='output/error.log', level=logging.ERROR)

    def test_proxy(proxy: str):
        with contextlib.suppress(Exception):
            response = requests.get(TEST_URL, proxies={'http': proxy}, timeout=TIMEOUT)
            if 100 <= response.status_code < 400:
                return proxy
        return None

    def main():
        start_time = time.time()
        http_proxies: List[str] = []

        with open(PROXY_LIST_FILE, 'r') as f:
            http_proxies = [line.strip() for line in f.readlines()]

        cpu_count = os.cpu_count() or 1
        max_threads = cpu_count * 420 or 1000

        print(f"[*] Utilizing {max_threads:,} threads, calculated from your device's {cpu_count} CPU cores.")

        with yaspin().bouncingBar as sp:
            sp.text = f"Initializing threads for {PROXY_LIST_FILE}..."
            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                import os
                import json
                import time
                import logging
                import asyncio
                import aiohttp
                from functools import lru_cache
                from typing import Dict, List
                from tqdm import tqdm


                def load_proxy_sources(file_path: str) -> Dict[str, List[str]]:
                    with open(file_path, 'r') as file:
                        return json.load(file)


                @lru_cache(maxsize=1)
                def proxy_sources() -> Dict[str, List[str]]:
                    # Cache disk reads; sources rarely change during a run.
                    return load_proxy_sources('proxy_sources.json')


                async def _check_proxies_async(proxies: List[str], test_url: str, proxy_scheme: str = 'http', concurrency: int = 200, timeout: int = 5) -> List[str]:
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

                        tasks = [check(p) for p in proxies]

                        for coro in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc=f"Checking ({proxy_scheme.upper()}) proxies", ascii=True, unit=" prox"):
                            result = await coro
                            if result:
                                valid.append(result)

                    return valid


                def _read_proxy_file(path: str) -> List[str]:
                    if not os.path.isfile(path):
                        return []
                    with open(path, 'r') as f:
                        return [line.strip() for line in f if line.strip()]


                def _write_proxy_file(path: str, proxies: List[str]):
                    with open(path, 'w') as f:
                        for p in proxies:
                            f.write(p + '\n')


                def _dedupe_preserve_order(proxies: List[str]) -> List[str]:
                    seen = set()
                    out: List[str] = []
                    for p in proxies:
                        if p not in seen:
                            seen.add(p)
                            out.append(p)
                    return out


                def http_check(PROXY_LIST_FILE: str, concurrency: int = 200, timeout: int = 5):
                    os.makedirs('output', exist_ok=True)
                    logging.basicConfig(filename='output/error.log', level=logging.ERROR)

                    TEST_URL = "http://httpbin.org/ip"

                    proxies = _read_proxy_file(PROXY_LIST_FILE)
                    if not proxies:
                        print(f"No proxies found in {PROXY_LIST_FILE}")
                        return

                    start = time.time()
                    valid = asyncio.run(_check_proxies_async(proxies, TEST_URL, proxy_scheme='http', concurrency=concurrency, timeout=timeout))
                    elapsed = time.time() - start

                    print(f"[*] Total time for Execution: {int(elapsed // 60)} minute(s) and {round(elapsed % 60, 2)} seconds")
                    print(f"[*] Valid HTTP Proxies: {len(valid):,}\n")

                    _write_proxy_file(PROXY_LIST_FILE, _dedupe_preserve_order(valid))


                def https_check(PROXY_LIST_FILE: str, concurrency: int = 200, timeout: int = 5):
                    os.makedirs('output', exist_ok=True)
                    logging.basicConfig(filename='output/error.log', level=logging.ERROR)

                    TEST_URL = "https://api.myip.com/"

                    proxies = _read_proxy_file(PROXY_LIST_FILE)
                    if not proxies:
                        print(f"No proxies found in {PROXY_LIST_FILE}")
                        return

                    start = time.time()
                    valid = asyncio.run(_check_proxies_async(proxies, TEST_URL, proxy_scheme='http', concurrency=concurrency, timeout=timeout))
                    elapsed = time.time() - start

                    print(f"[*] Total time for Execution: {int(elapsed // 60)} minute(s) and {round(elapsed % 60, 2)} seconds")
                    print(f"[*] Valid HTTPS Proxies: {len(valid):,}")

                    _write_proxy_file(PROXY_LIST_FILE, _dedupe_preserve_order(valid))
