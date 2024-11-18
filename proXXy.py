#!/usr/bin/python3
# Built by Solanaceae -- https://solanaceae.xyz/
import os
import re
import json
import time
import yaml
import utils
import shutil
import random
import pystyle
import logging
import argparse
import platform
import hrequests
import src_check
import subprocess
from yaspin import yaspin
from urllib.parse import urlparse
from scrapy import Spider, Request
from scrapy.crawler import CrawlerProcess

def banner(script_version):
    banner = r"""
                     _  ___  __     
    ____  _________ | |/ / |/ /_  __
   / __ \/ ___/ __ \|   /|   / / / /
  / /_/ / /  / /_/ /   |/   / /_/ / 
 / .___/_/   \____/_/|_/_/|_\__, /  
/_/                        /____/   """

    os.system("title proXXy -- by Solanaceae")
    os.system('cls' if os.name == 'nt' else 'clear')
    text = f"{script_version}\nby Solanaceae\nhttps://solanaceae.xyz/"
    print(pystyle.Add.Add(banner, text, 4))
    print()
    print(vanity_line())

def vanity_line():
    try:
        terminal_width = shutil.get_terminal_size().columns
    except OSError:
        terminal_width = 80
    dash = "—"
    dashes = dash * (terminal_width - 2)
    return f"<{dashes}>"

def init_logging():
    try:
        logging.basicConfig(filename=os.path.join('output/error.log'), level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Application started.")
    except Exception as e:
        print(f"Failed to initialize logging: {e}")

def init_spinner():
    banner(script_version)
    with yaspin().bouncingBar as sp:
        sp.text = "Initializing..."
        time.sleep(2.5)
        sp.ok("[_OK_]")
        time.sleep(1.5)

def check_url_validity(url, timeout=5):
    global response_time_ms
    try:
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            logging.error(f"Invalid URL format: {url}")
            return False, None

        response = hrequests.get(url, nohup=True, timeout=timeout)
        response_time_ms = round(response.elapsed.total_seconds() * 1000, 1)
        
        if response.status_code == 200:
            return True, response_time_ms
        else:
            return False, None
    except Exception as e:
        logging.error(f"Error checking URL {url}: {e}")
        return False, None

def validate_proxies(proxy_sources, output_dir="validated", timeout=5):
    os.makedirs(output_dir, exist_ok=True)
    valid_urls, invalid_urls = {}, {}

    start_time = time.time()
    url_width = 120

    for protocol, urls in proxy_sources.items():
        print(f"{protocol} source checking...\n")

        valid_urls[protocol] = []
        invalid_urls[protocol] = []

        responses = hrequests.get(urls, nohup=True, timeout=timeout)

        for i, response in enumerate(responses):
            url = urls[i]
            cleaned_url = f"{url.split('//')[-1]:<{url_width}}"

            try:
                response_time_ms = round(response.elapsed.total_seconds() * 1000, 1)

                if response.status_code == 200:
                    print(f'{pystyle.Colorate.Color(pystyle.Colors.green, f"[+] VALID: {cleaned_url}", True)} || {response_time_ms:,} ms')
                    valid_urls[protocol].append({'url': url, 'response_time_ms': response_time_ms})
                else:
                    print(f'{pystyle.Colorate.Color(pystyle.Colors.red, f"[-] INVALID: {cleaned_url}", True)}| ERROR')
                    invalid_urls[protocol].append({'url': url, 'response_time_ms': response_time_ms})

                time.sleep(0.05)
            except Exception as e:
                logging.error(f"Error processing URL {url}: {e}")
                print(
                    f'{pystyle.Colorate.Color(pystyle.Colors.red, f"[-] INVALID: {cleaned_url}", True)}| ERROR'
                )
                invalid_urls[protocol].append({'url': url, 'response_time_ms': None})

        time.sleep(0.5)
        banner(script_version)

    valid_file_path = os.path.join(output_dir, 'VALID.yaml')
    invalid_file_path = os.path.join(output_dir, 'INVALID.yaml')

    with open(valid_file_path, 'w') as file:
        yaml.dump(valid_urls, file)

    with open(invalid_file_path, 'w') as file:
        yaml.dump(invalid_urls, file)

    report_validation_summary(valid_file_path, invalid_file_path, start_time)

def save_proxies(proxy_list, file_path):
    with open(file_path, 'w') as file:
        file.writelines(f"{url}\n" for url in proxy_list)

def load_yaml(file_path):
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        return {}
    with open(file_path, 'r') as file:
        return yaml.safe_load(file) or {}

def report_validation_summary(valid_file_path, invalid_file_path, start_time):
    valid_urls = load_yaml(valid_file_path)
    invalid_urls = load_yaml(invalid_file_path)

    accessed = sum(len(url_list) for url_list in valid_urls.values())
    not_accessed = sum(len(url_list) for url_list in invalid_urls.values())

    elapsed_time = round(time.time() - start_time, 2)

    print(f"Validation complete: {accessed} valid URLs, {not_accessed} invalid URLs.")
    print(f"Time taken: {elapsed_time} seconds")
    print(vanity_line())

    logging.info(f"Validation summary: {accessed} valid URLs, {not_accessed} invalid URLs in {elapsed_time} seconds")

class ProxySpider(Spider):
    name = 'proxy_spider'
    custom_settings = {
        'LOG_LEVEL': 'ERROR', # https://docs.scrapy.org/en/latest/topics/logging.html
        'DOWNLOAD_TIMEOUT': 5,
        'RETRY_TIMES': 2,
        'RETRY_HTTP_CODES': [500, 502, 503, 504, 408],
    }

    def start_requests(self):
        sources = utils.proxy_sources()
        for protocol, urls in sources.items():
            for url in urls:
                yield Request(url, callback=self.parse, meta={'protocol': protocol})

    def parse(self, response):
        protocol = response.meta['protocol']
        proxies = self.extract_proxies(response.text)
        self.save_proxies(protocol, proxies)

    def extract_proxies(self, html_content):
        proxy_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+')
        return proxy_pattern.findall(html_content)

    def save_proxies(self, protocol, proxies):
        os.makedirs("output", exist_ok=True)
        file_path = f"output/{protocol}.txt"
        with open(file_path, 'a') as file:
            for proxy in proxies:
                file.write(f"{proxy}\n")

def proxy_scrape():
    global total_scraped
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Ubuntu 20.04; rv:89.0) Gecko/20100101 Firefox/89.0"
    ]

    process = CrawlerProcess(settings={'USER_AGENT': random.choice(user_agents)})
    process.crawl(ProxySpider)
    process.start()

    output_files = ['output/HTTP.txt', 'output/HTTPS.txt', 'output/SOCKS4.txt', 'output/SOCKS5.txt']
    total_scraped = sum(count_lines(file) for file in output_files)
    
    print(f'\n[+] {total_scraped:,} proxies scraped.')


def count_lines(file_path):
    if not os.path.isfile(file_path):
        logging.error(f"File not found: {file_path}")
        return 0

    try:
        with open(file_path, 'r') as file:
            return sum(1 for _ in file)
    except IOError as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return 0

 
def proxy_clean(http_file, https_file, socks4_file, socks5_file):
    def remove_duplicates(input_file):
        with open(input_file, 'r') as file:
            unique_proxies = set(file.readlines())

        with open(input_file, 'w') as file:
            file.writelines(unique_proxies)

    proxy_files = [http_file, https_file, socks4_file, socks5_file]
    output_files = ['output/HTTP.txt', 'output/HTTPS.txt', 'output/SOCKS4.txt', 'output/SOCKS5.txt']

    for file in proxy_files:
        remove_duplicates(file)

    total_sanitized = sum(count_lines(output) for output in output_files)
    total = total_scraped - total_sanitized

    print(f"[+] {total:,} proxies sanitized.")
    print(vanity_line())

def run_update_script(script_version):
    current_os = platform.system()
    update_folder = os.path.join(os.path.dirname(__file__), 'update')
    env = os.environ.copy()
    env['SCRIPT_VERSION'] = script_version

    try:
        if current_os in ['Linux', 'Darwin']:
            update_script = os.path.join(update_folder, 'update.sh')
            subprocess.run(['chmod', '+x', update_script], check=True)
            subprocess.run([update_script], env=env, check=True)
        elif current_os == 'Windows':
            update_script = os.path.join(update_folder, 'update.ps1')
            command = ['powershell', '-ExecutionPolicy', 'Bypass', '-File', update_script]
            subprocess.run(command, env=env, check=True)
        else:
            logging.error(f"Unsupported OS: {current_os}")
            print('[-] Unsupported operating system.')
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to run update script: {e}")
        print("[-] Update failed. Check logs for details.")

def check_for_update(script_version):
    banner(script_version)
    api_url = (
        "https://api.github.com/repos/Atropa-Solanaceae/proXXy/releases/latest"
    )

    try:
        response = hrequests.get(api_url)

        if response.status_code == 200:
            return update_notif(response, script_version)
        print(f"[-] Failed to check for updates. HTTP Status Code: {response.status_code}")
        return False
    except Exception as e:
        print(f"[-] Error checking for updates: {e}")
        return False

def update_notif(response, script_version):
    release_info = json.loads(response.text)
    latest_version = release_info['tag_name']

    if script_version >= latest_version:
        return False
    print(f"[+] A new version is available: {latest_version}. You are running {script_version}.")
    print("[+] Please update your script to the latest version by using the -u flag.")
    return True
    
def main():
    global script_version
    script_version = 'v2.6'
    parser = argparse.ArgumentParser(description='A super simple asynchronous multithreaded proxy scraper; scraping & checking ~500k HTTP, HTTPS, SOCKS4, & SOCKS5 proxies.')
    parser.add_argument('--validate', '-V', action='store_true', help='Flag to validate proxies after scraping (default: False)')
    parser.add_argument('--update', '-u', action='store_true', help='Flag to run the update script and then exit')
    parser.add_argument('--version', '-v', action='version', version=f'%(prog)s {script_version}', help='Print the version of the script and exit')
    parser.add_argument('--src_check', '-s', action='store_true', help='Flag to verify sources')
    args = parser.parse_args()

    if args.update:
        run_update_script(script_version)
        return

    if check_for_update(script_version):
        time.sleep(2.5)
        
    if args.src_check:
        src_check.main()
        return

    for filename in ['output/HTTP.txt', 'output/HTTPS.txt', 'output/SOCKS4.txt', 'output/SOCKS5.txt']: open(filename, 'w').close()

    init_logging()
    init_spinner()
    banner(script_version)
    proxies = utils.proxy_sources()

    validate_proxies(proxies)

    proxy_scrape()
    proxy_clean('output/HTTP.txt', 'output/HTTPS.txt', 'output/SOCKS4.txt', 'output/SOCKS5.txt')

    if args.validate:
        utils.http_check('output/HTTP.txt')
        utils.https_check('output/HTTPS.txt')
        print(vanity_line())

if __name__ == "__main__":
    main()
