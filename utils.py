import contextlib
import os
import json
import time
import logging
import requests
from tqdm import tqdm
from yaspin import yaspin
from concurrent.futures import ThreadPoolExecutor

def load_proxy_sources(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def proxy_sources():
    return load_proxy_sources('proxy_sources.json')

def http_check(PROXY_LIST_FILE): 
    # combine two methods into one, so that when it's called it'll differentiate based upon what type of proxy parameter is fed into it
    TEST_URL = "http://httpbin.org/ip" # https://httpbin.org/anything # https://api.myip.com/ #FIXME add in time to reach judge sites in milliseconds
    TIMEOUT = 5
    logging.basicConfig(filename='output/error.log', level=logging.ERROR)

    def test_proxy(proxy):
        with contextlib.suppress(Exception):
            response = requests.get(TEST_URL, proxies={'http': proxy}, timeout=TIMEOUT)
            if 100 <= response.status_code < 400:
                return proxy
        return None

    def main():
        start_time = time.time()
        http_proxies = []

        with open(PROXY_LIST_FILE, 'r') as f:
            http_proxies = [line.strip() for line in f.readlines()]

        cpu_count = os.cpu_count()
        max_threads = cpu_count * 420 or 1000

        print(f"[*] Utilizing {max_threads:,} threads, calculated from your device's {cpu_count} CPU cores.")

        with yaspin().bouncingBar as sp:
            sp.text = f"Initializing threads for {PROXY_LIST_FILE}..."
            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                results = []
                progress_started = False
                for result in tqdm(executor.map(test_proxy, http_proxies), total=len(http_proxies), desc="[*] Checking HTTP Proxies", ascii=" #", unit= " prox"):
                    if not progress_started:
                        sp.text = "Threads initialized."
                        sp.ok("[_OK_]")
                        sp.stop()
                        progress_started = True
                    results.append(result)

        http_valid_proxies = [proxy for proxy in results if proxy is not None]

        end_time = time.time()
        total_time = end_time - start_time
        total_minutes = total_time // 60
        remaining_seconds = total_time % 60
        print("[*] Total time for Execution:", f"{int(total_minutes)} minute(s) and {round(remaining_seconds, 2)} seconds")

        print(f"[*] Valid HTTP Proxies: {len(http_valid_proxies):,}\n")

        with open(PROXY_LIST_FILE, 'w') as f:
            for proxy in http_valid_proxies:
                f.write(proxy + '\n')

    main()
    
def https_check(PROXY_LIST_FILE):
    # FIXME tell the user the anonymity level of the proxy
    # FIXME add in socks4/5 verification
    TEST_URL = "https://api.myip.com:443/"
    TIMEOUT = 5
    logging.basicConfig(filename='error.log', level=logging.ERROR)

    def test_proxy(proxy):
        with contextlib.suppress(Exception):
            response = requests.get(TEST_URL, proxies={'https': proxy}, timeout=TIMEOUT)
            if 100 <= response.status_code < 400:
                return proxy
        return None

    def main():
        start_time = time.time()
        https_proxies = []

        with open(PROXY_LIST_FILE, 'r') as f:
            https_proxies = [line.strip() for line in f.readlines()]

        cpu_count = os.cpu_count()
        max_threads = cpu_count * 250 or 1000

        print(f"[*] Utilizing {max_threads:,} threads, calculated from your device's {cpu_count} CPU cores.")

        with yaspin().bouncingBar as sp:
            sp.text = f"Initializing threads for {PROXY_LIST_FILE}..."
            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                results = []
                progress_started = False
                for result in tqdm(executor.map(test_proxy, https_proxies), total=len(https_proxies), desc="[*] Checking HTTPS Proxies", ascii=" #", unit= " prox"):
                    if not progress_started:
                        sp.text = "Threads initialized."
                        sp.ok("[_OK_]")
                        sp.stop()
                        progress_started = True
                    results.append(result)

        https_valid_proxies = [proxy for proxy in results if proxy is not None]

        end_time = time.time()
        total_time = end_time - start_time
        total_minutes = total_time // 60
        remaining_seconds = total_time % 60
        print("[*] Total time for Execution:", f"{int(total_minutes)} minute(s) and {round(remaining_seconds, 2)} seconds")

        print(f"[*] Valid HTTPS Proxies: {len(https_valid_proxies):,}")

        with open(PROXY_LIST_FILE, 'w') as f:
            for proxy in https_valid_proxies:
                f.write(proxy + '\n')

    main()
