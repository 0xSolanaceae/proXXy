#!/usr/bin/python3
# Built by Solanaceae -- https://solanaceae.xyz/
import os
import re
import time
#from build import utils
import utils
import shutil
import pystyle
import logging
import argparse
import platform
import subprocess
from yaspin import yaspin
from hrequests import session
from scrapy import Spider, Request
from scrapy.crawler import CrawlerProcess

def banner():
    banner = r"""
 ▄████████   ▄██████▄   ▄█         ▄████████  ███▄▄▄▄      ▄████████  ▄████████    ▄████████    ▄████████    ▄████████ 
  ███    ███ ███    ███ ███        ███    ███ ███▀▀▀██▄   ███    ███ ███    ███   ███    ███   ███    ███   ███    ███ 
  ███    █▀  ███    ███ ███        ███    ███ ███   ███   ███    ███ ███    █▀    ███    █▀    ███    ███   ███    █▀  
  ███        ███    ███ ███        ███    ███ ███   ███   ███    ███ ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄     
▀███████████ ███    ███ ███      ▀███████████ ███   ███ ▀███████████ ███        ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀     
         ███ ███    ███ ███        ███    ███ ███   ███   ███    ███ ███    █▄    ███    █▄    ███    ███   ███    █▄  
   ▄█    ███ ███    ███ ███▌    ▄  ███    ███ ███   ███   ███    ███ ███    ███   ███    ███   ███    ███   ███    ███ 
 ▄████████▀   ▀██████▀  █████▄▄██  ███    █▀   ▀█   █▀    ███    █▀  ████████▀    ██████████   ███    █▀    ██████████"""

    os.system("title proXXy -- by Solanaceae")
    os.system('cls' if os.name == 'nt' else 'clear')
    print((pystyle.Colorate.Vertical(pystyle.Colors.purple_to_blue, banner, 1)))
    print()
    print(vanity_line())

def vanity_line():
    terminal_width = shutil.get_terminal_size().columns
    dash = "—"
    dashes = dash * (terminal_width - 2)
    return f"<{dashes}>"

def init():
    os.system('cls' if os.name == 'nt' else 'clear')
    logging.basicConfig(filename='output/error.log', level=logging.ERROR)
    with yaspin().bouncingBar as sp:
        sp.text = "Initializing..."
        time.sleep(2.5)
        sp.ok("[_OK_]")
        time.sleep(1.5)

def check_url_validity(url):
    try:
        response = session.get(url, timeout=1)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"Error: {e}\n")
        return False

def validate_proxies(proxy_sources):
    valid_urls = []
    invalid_urls = []

    start_time = time.time()
    
    for protocol, urls in proxy_sources.items():
        print(f"\nValidating {protocol} proxy urls...\n")
        for url in urls:
            cleaned_url = url.split("//")[-1]
            if check_url_validity(url):
                print(f"[+] VALID: {cleaned_url}")
                valid_urls.append(url)
            else:
                print(f"[-] INVALID: {cleaned_url}")
                invalid_urls.append(url)
                
    with open("validated/VALID.txt", 'w') as valid_file:
        for valid_url in valid_urls:
            valid_file.write(f"{valid_url}\n")

    with open("validated/INVALID.txt", 'w') as invalid_file:
        for invalid_url in invalid_urls:
            invalid_file.write(f"{invalid_url}\n")
            
    if not valid_urls:
        print("\n[-] A network error may have occurred, as no urls were found valid. Please ensure your device is connected to the internet.\n")
        exit()
    
    accessed = len(valid_urls)
    not_accessed = len(invalid_urls)
    print(f"\nValidation complete, {accessed:,} URL(s) accessed, {not_accessed:,} URL(s) not accessed.\n")
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time = round(elapsed_time, 2)
    print(f"Time taken to validate all URLs: {elapsed_time} seconds")
    print(vanity_line())
    time.sleep(1)
    return valid_urls, invalid_urls

class ProxySpider(Spider):
    name = 'proxy_spider'
    custom_settings = {
        'LOG_LEVEL': 'ERROR',
    }

    def start_requests(self):
            sources = utils.cproxy_sources()
            for protocol, urls in sources.items():
                for url in urls:
                    try:
                        yield Request(url, callback=self.parse, meta={'protocol': protocol})
                    except ValueError:
                        pass
                
    def parse(self, response):
        protocol = response.meta['protocol']
        proxies = self.extract_proxies(response.text)
        self.save_proxies(protocol, proxies)

    def extract_proxies(self, html_content):
        proxy_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+')
        proxies = proxy_pattern.findall(html_content)
        
        return proxies

    def save_proxies(self, protocol, proxies):
        filename = f"output/{protocol}.txt"
        with open(filename, 'a') as file:
            for proxy in proxies:
                file.write(f"{proxy}\n")

def proxy_scrape():
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    })

    process.crawl(ProxySpider)
    process.start()
    time.sleep(1)

    http_lines = count_lines('output/HTTP.txt')
    https_lines = count_lines('output/HTTPS.txt')
    socks4_lines = count_lines('output/SOCKS4.txt')
    socks5_lines = count_lines('output/SOCKS5.txt')
    
    total = http_lines + https_lines + socks4_lines + socks5_lines
    print(f'\n[+] {total:,} Proxies scraped.')

def count_lines(file_path):
        with open(file_path, 'r') as file:
            return sum(1 for line in file)
 
def proxy_clean(http_file, https_file, socks4_file, socks5_file):
    def remove_duplicates(input_file, output_file):
        with open(input_file, 'r') as file:
            unique_proxies = set(file.readlines())

        with open(output_file, 'w') as file:
            file.writelines(unique_proxies)

    remove_duplicates(http_file, http_file)
    remove_duplicates(https_file, https_file)
    remove_duplicates(socks4_file, socks4_file)
    remove_duplicates(socks5_file, socks5_file)

    http_lines = count_lines('output/HTTP.txt')
    https_lines = count_lines('output/HTTPS.txt')
    socks4_lines = count_lines('output/SOCKS4.txt')
    socks5_lines = count_lines('output/SOCKS5.txt')
    
    total = http_lines + https_lines + socks4_lines + socks5_lines
    
    print(f"[+] {total:,} Proxies sanitized.\n")
    print(vanity_line())

def run_update_script():
    current_os = platform.system()
    update_folder = os.path.join(os.path.dirname(__file__), 'update')

    if current_os == 'Linux' or current_os == 'Darwin':
        update_script = os.path.join(update_folder, 'update.sh')
        subprocess.run(['chmod', '+x', update_script], check=True)
        subprocess.run([update_script], check=True)
    elif current_os == 'Windows':
        update_script = os.path.join(update_folder, 'update.bat')
        subprocess.run([update_script], check=True)
    else:
        print('[-] Unsupported operating system.')

def main():
    parser = argparse.ArgumentParser(description='A super simple asynchronous multithreaded proxy scraper; scraping & checking ~500k HTTP, HTTPS, SOCKS4, & SOCKS5 proxies.')
    parser.add_argument('--validate', '-v', action='store_true', help='Flag to validate proxies after scraping (default: False)')
    parser.add_argument('--update', '-u', action='store_true', help='Flag to run the update script and then exit')
    parser.add_argument('--version', '-V', action='version', version='%(prog)s v2.4', help='Print the version of the script and exit')
    args = parser.parse_args()
    
    if args.update:
        run_update_script()
        return
    
    if args.validate and args.update:
        print("Error: The '--validate' flag cannot be used in conjunction with the '--update' flag.")
        return
    
    init()
    banner()
    proxies = utils.cproxy_sources()
    
    validate_proxies(proxies)
    
    proxy_scrape()
    proxy_clean('output/HTTP.txt', 'output/HTTPS.txt', 'output/SOCKS4.txt', 'output/SOCKS5.txt')
    
    if args.validate:
        utils.chttp_check('output/HTTP.txt')
        utils.chttps_check('output/HTTPS.txt')
    
    print("\n[+] proXXy has finished validating, scraping, and sanitizing proxies.\n")
    print(vanity_line())

if __name__ == "__main__":
    main()
