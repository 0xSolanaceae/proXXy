#!/usr/bin/python3
# Built by Solanaceae -- https://solanaceae.xyz/
import os
import pystyle
import time
import shutil
import re
import logging
import argparse
from hrequests import session
from yaspin import yaspin
from scrapy.crawler import CrawlerProcess
from scrapy import Spider, Request
from platform import system as platform_system
from proxy_check import http_check, https_check

def proxy_sources():
    return {
        "HTTP": [
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://api.openproxylist.xyz/http.txt",
            "https://alexa.lr2b.com/proxylist.txt",
            "https://multiproxy.org/txt_all/proxy.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
            "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
            "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
            "https://rootjazz.com/proxies/proxies.txt",
            "https://spys.me/proxy.txt",
            "https://proxyspace.pro/http.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt",
            "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
            "https://sunny9577.github.io/proxy-scraper/proxies.txt",
            "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
            "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
            "https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt",
            "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt",
            "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
            "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
        ],
        "SOCKS4": [
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4",
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
            "https://api.openproxylist.xyz/socks4.txt",
            "https://proxyspace.pro/socks4.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks4.txt",
            "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt",
            "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt",
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",
            "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt",
            "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt",
            "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
            "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt"
        ],
        "SOCKS5": [
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
            "https://api.openproxylist.xyz/socks5.txt",
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5",
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5",
            "https://proxyspace.pro/socks5.txt",
            "https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks5.txt",
            "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt",
            "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt",
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
            "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt",
            "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt",
            "https://spys.me/socks.txt",
            "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt",
            "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt"
        ],
        "HTTPS": [
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
            "https://proxyspace.pro/https.txt",
            "https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt",
            "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
            "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt"
        ]
    }

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
    logging.basicConfig(filename='error.log', level=logging.ERROR)
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
        print("[-] A network error may have occurred, as no urls were found valid. Please ensure your device is connected to the internet.\n")
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
            sources = proxy_sources()
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
    def count_lines(file_path):
        with open(file_path, 'r') as file:
            return sum(1 for line in file)

    http_lines = count_lines('output/HTTP.txt')
    https_lines = count_lines('output/HTTPS.txt')
    socks4_lines = count_lines('output/SOCKS4.txt')
    socks5_lines = count_lines('output/SOCKS5.txt')
    
    total = http_lines + https_lines + socks4_lines + socks5_lines
    print(f'\n[+] {total:,} Proxies scraped.')
        
def proxy_clean(http_file, https_file, socks4_file, socks5_file):
    def remove_duplicates(input_file, output_file):
        with open(input_file, 'r') as file:
            unique_proxies = set(file.readlines())

        with open(output_file, 'w') as file:
            file.writelines(unique_proxies)
    
    def port_filter(input_file, output_file):
        with open(input_file, 'r') as file:
            lines = file.readlines()

        filtered_lines = [line.strip() for line in lines if not (line.strip().endswith(":1080") or line.strip().endswith(":5555"))]

        with open(input_file, 'w') as output_file:
            output_file.write('\n'.join(filtered_lines))

    remove_duplicates(http_file, http_file)
    remove_duplicates(https_file, https_file)
    remove_duplicates(socks4_file, socks4_file)
    remove_duplicates(socks5_file, socks5_file)
    port_filter(http_file, http_file)
    port_filter(https_file, https_file)
    port_filter(socks4_file, socks4_file)
    port_filter(socks5_file, socks5_file)
    
    def count_lines(file_path):
        with open(file_path, 'r') as file:
            return sum(1 for line in file)

    http_lines = count_lines('output/HTTP.txt')
    https_lines = count_lines('output/HTTPS.txt')
    socks4_lines = count_lines('output/SOCKS4.txt')
    socks5_lines = count_lines('output/SOCKS5.txt')
    
    total = http_lines + https_lines + socks4_lines + socks5_lines
    
    print(f"[+] {total:,} Proxies sanitized.\n")
    print(vanity_line())

def run_update_script():
    current_os = platform_system()
    if (
        current_os == 'Linux'
        or current_os != 'Windows'
        and current_os == 'Darwin'
    ):
        os.run(['chmod', '+x', 'update.sh'])
        os.run(['./update.sh'])
    elif current_os == 'Windows':
        os.run(['update.bat'])
    else:
        print('Unsupported operating system.')

def main():
    parser = argparse.ArgumentParser(description='A super simple multithreaded proxy scraper; scraping & checking ~500k HTTP, HTTPS, SOCKS4, & SOCKS5 proxies.')
    parser.add_argument('--validate', '-v', action='store_true', help='Flag to validate proxies after scraping (default: False)')
    parser.add_argument('--update', '-u', action='store_true', help='Flag to run the update script and then exit')

    args = parser.parse_args()
    
    if args.update:
        run_update_script()
        return
    
    if args.validate and args.update:
        print("Error: The '--validate' flag cannot be used in conjunction with the '--update' flag.")
        return
    
    init()
    banner()
    proxies = proxy_sources()
    
    validate_proxies(proxies)
    
    proxy_scrape()
    proxy_clean('output/HTTP.txt', 'output/HTTPS.txt', 'output/SOCKS4.txt', 'output/SOCKS5.txt')
    
    if args.validate:
        http_check('output/HTTP.txt')
        https_check('output/HTTPS.txt')
    
    print("\n[+] proXXy has finished validating, scraping, and sanitizing proxies.\n")
    print(vanity_line())

if __name__ == "__main__":
    main()
