#!/usr/bin/python3
#Coded by Solanaceae
import os
import re
import shutil
import socket
import random
import requests
import warnings
import platform
import argparse
import threading
import contextlib
import subprocess
from bs4 import BeautifulSoup
from pystyle import *

def proxy_sources():
    return {
        "HTTP": [
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt",
            "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
            "https://api.openproxylist.xyz/http.txt",
            "http://alexa.lr2b.com/proxylist.txt",
            "https://multiproxy.org/txt_all/proxy.txt",
            "https://proxyspace.pro/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
            "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
            "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
            "http://rootjazz.com/proxies/proxies.txt",
            "http://spys.me/proxy.txt",
            "https://proxyspace.pro/http.txt",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt",
            "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
            "https://sunny9577.github.io/proxy-scraper/proxies.txt",
            "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
            "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
            "https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt",
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
            "https://proxyspace.pro/socks4.txt",
            "https://www.proxy-list.download/api/v1/get?type=socks4",
            "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks4.txt",
            "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt",
            "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt",
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",
            "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt",
            "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt",
            "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt"
        ],
        "SOCKS5": [
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
            "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt",
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
            "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt"
        ],
        "HTTPS": [
            "http://sslproxies.org",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
            "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt",
            "https://proxyspace.pro/https.txt",
            "https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt",
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
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue, banner, 1)))
    print()
    

def parameters():
    global rand_UA
    global timeout
    global prox_check
    global user_agents

    try:
        banner()
        prox_check_input = input("Would you like to check proxies? (Y/n): ").lower()
        if prox_check_input == "":
            raise Exception
        prox_check = prox_check_input.lower() != "n"
    except Exception:
        prox_check = True

    if prox_check:
        try:
            banner()
            rand_UA_input = input("Would you like to use random user agents? (Y/n): ").lower()
            if rand_UA_input == "":
                raise Exception
            rand_UA = rand_UA_input.lower() != "n"
        except Exception:
            rand_UA = True

        try:
            banner()
            timeout_input = input("How long should the request timeout be? (Default is 10 seconds, cannot be lower than 5): ")
            if timeout_input == "":
                raise Exception
            timeout_input = int(timeout_input)
            timeout = timeout_input if timeout_input >= 5 else 10
        except Exception:
            timeout = 10
    else:
        timeout = None
        rand_UA = None

    if rand_UA:
        user_agents = []
        with open("user_agents.txt", "r") as file:
            user_agents = file.read().splitlines()

    # Confirmation prompt
    banner()
    print(f"Selected option(s):\n\n -- Proxy check: {prox_check}")
    if rand_UA is not None:
        print(f" -- Random user agents: {rand_UA}")
    if timeout is not None:
        print(f" -- Timeout: {timeout}")
    confirm_input = input("\nDo you want to continue? (Y/n): ").lower()

    # Check user's confirmation
    if confirm_input == "n":
        parameters()

## proxy processing

def remove_duplicate_proxies(protocol):
    # Read in the text document
    try:
        with open(f'scraped/{protocol}.txt', 'r') as file:
            proxies_data = file.read()
    except IOError:
        print(f"Error: Could not read {protocol}.txt")
        return

    # Split the proxies into a list and remove duplicates
    proxies = proxies_data.splitlines()
    unique_proxies = list(set(proxies))

    # Overwrite the original text document with the unique proxies
    try:
        with open(f'scraped/{protocol}.txt', 'w') as file:
            for proxy in unique_proxies:
                file.write(proxy + '\n')
    except IOError:
        print(f"Error: Could not write to {protocol}.txt")
        return
    
def regularize_proxies(protocol):
    try:
        with open(f'scraped/{protocol}.txt', 'r') as file:
            text_data = file.read()
            lines = file.readlines()
    except IOError:
        print(f"Error: Could not read {protocol}.txt")
        return

    # Define a regex pattern to match proxies
    proxy_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+'
    proxies = re.findall(proxy_pattern, text_data)

    # Overwrite the original text document with the regularized proxies
    try:
        with open(f'scraped/{protocol}.txt', 'w') as file:
            file.write('\n'.join(lines)) #remove empty lines
            for proxy in proxies:
                file.write(proxy + '\n')

    except IOError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(vanity_line)
        print(f"\nError: Could not write to {protocol}.txt\n")
        exit_con()

## checking portion

def SOCKS4_check(site, timeout, rand_UA):
    pass

def SOCKS5_check(site, timeout, rand_UA):
    pass

def HTTP_check(site, timeout, rand_UA):
    import tqdm
    
    PROXY_LIST_FILE = 'scraped/HTTP.txt'
    TEST_URL = site
    TIMEOUT = timeout

    def test_proxy(proxy, results):
        with contextlib.suppress(requests.exceptions.RequestException, socket.timeout):
            headers = {}
            if rand_UA:
                headers['User-Agent'] = random.choice(user_agents)
            else:
                headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'

            response = requests.get(TEST_URL, proxies={'http': proxy}, headers=headers, timeout=TIMEOUT)
            if response.status_code == 200:
                results.append(proxy)

    http_proxies = []
    http_valid_proxies = []
    with open(PROXY_LIST_FILE, 'r') as f:
        http_proxies = [line.strip() for line in f.readlines()]

    threads = []
    for proxy in tqdm.tqdm(http_proxies, desc="Checking HTTP Proxies", ascii=" #", unit= " prox"):
        thread = threading.Thread(target=test_proxy, args=(proxy, http_valid_proxies), daemon=True)
        threads.append(thread)
        thread.start()

    for thread in tqdm.tqdm(threads, desc="Joining Threads", ascii=" #", unit= " thr"):
        thread.join()

    with open(PROXY_LIST_FILE, 'w') as f:
        for proxy in http_valid_proxies:
            f.write(proxy + '\n')
    
def HTTPS_check(site, timeout, rand_UA):
    import tqdm
    
    PROXY_LIST_FILE = 'scraped/HTTPS.txt'
    TEST_URL = site
    TIMEOUT = timeout

    def test_proxy(proxy, results):
        with contextlib.suppress(requests.exceptions.RequestException, socket.timeout):
            headers = {}
            if rand_UA:
                headers['User-Agent'] = random.choice(user_agents)
            else:
                headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'

            response = requests.get(TEST_URL, proxies={'https': proxy}, headers=headers, timeout=TIMEOUT)
            if response.status_code == 200:
                results.append(proxy)

    https_proxies = []
    https_valid_proxies = []
    with open(PROXY_LIST_FILE, 'r') as f:
        https_proxies = [line.strip() for line in f.readlines()]

    threads = []
    #for proxy in tqdm.tqdm(proxies, desc="Checking HTTPS Proxies", ascii=" #", unit= " prox"):
    ##    thread = threading.Thread(target=test_proxy, args=(proxy, https_valid_proxies), daemon=True)
    #    threads.append(thread)
    #    thread.start()

    for thread in tqdm.tqdm(threads, desc="Joining Threads", ascii=" #", unit= " thr"):
        thread.join()

    with open(PROXY_LIST_FILE, 'w') as f:
        for proxy in https_valid_proxies:
            f.write(proxy + '\n')

## proxy scraping

def scrape_url(url, proxy_type, error_log):
    global accessed_sources
    global total_sources

    total_sources += 1

    try:
        response = requests.get(url)
        if response.status_code == 200:
            accessed_sources += 1
            soup = BeautifulSoup(response.content, 'html.parser')
            scraped_data = soup.get_text()
            if proxy_type == "HTTP":
                with open("scraped/HTTP.txt", "a") as file_http:
                    file_http.write(scraped_data + '\n')
            elif proxy_type == "SOCKS4":
                with open("scraped/SOCKS4.txt", "a") as file_socks4:
                    file_socks4.write(scraped_data + '\n')
            elif proxy_type == "SOCKS5":
                with open("scraped/SOCKS5.txt", "a") as file_socks5:
                    file_socks5.write(scraped_data + '\n')
            elif proxy_type == "HTTPS":
                with open("scraped/HTTPS.txt", "a") as file_https:
                    file_https.write(scraped_data + '\n')
        else:
            error_log.write(f"Could not access: {url}\n")
    except Exception as e:
        error_log.write(f"Could not access: {url}")
        error_log.write(f"Error message: {str(e)}\n")

def scraping_handler(error_log, site, timeout):
    import tqdm
    global accessed_sources
    global total_sources

    print(vanity_line)

    # proxy sources
    proxies = proxy_sources()

    total_sources = 0
    accessed_sources = 0

    threads = []
    # webscraping proxies
    for proxy_type, urls in tqdm.tqdm(proxies.items(), desc="Scraping Sources", ascii=" #", unit=" src"):
        for url in urls:
            thread = threading.Thread(target=scrape_url, args=(url, proxy_type, error_log))
            thread.start()
            threads.append(thread)

    # Wait for all threads to finish
    for thread in tqdm.tqdm(threads, desc="Joining Threads", ascii=" #", unit= " thr"):
        thread.join()
    print()

    if accessed_sources == 0:
        error = "|| A network error occured, please ensure your device is connected to the internet. ||"

        empty_space = terminal_width - len(error)
        left_space = empty_space // 2
        right_space = empty_space - left_space

        os.system('cls' if os.name == 'nt' else 'clear')
        print(vanity_line)
        print(" " * left_space + error + " " * right_space)
        exit_con()
    elif accessed_sources < total_sources:
        error = "|| Some sources could not be accessed, please check the logfile for more details. ||"

        empty_space = terminal_width - len(error)
        left_space = empty_space // 2
        right_space = empty_space - left_space
        print(" " * left_space + error + " " * right_space)


    percentage = accessed_sources / total_sources * 100
    info = f"|| Total Sources: {total_sources} || Accessed Sources: {accessed_sources} || ({percentage:.2f}%) ||"

    # Calculate the remaining empty space on the left and right
    empty_space = terminal_width - len(info)
    left_space = empty_space // 2
    right_space = empty_space - left_space

    print(" " * left_space + info + " " * right_space)
    print()

    protocols = ["SOCKS4", "SOCKS5", "HTTP", "HTTPS"]
    for protocol in tqdm.tqdm(protocols, desc="Regularizing Proxies", ascii=" #", unit= " prox"):
        regularize_proxies(protocol)
    for protocol in tqdm.tqdm(protocols, desc="Removing Duplicates", ascii=" #", unit= " prox"):
        remove_duplicate_proxies(protocol)
    print()

    if prox_check:
        for protocol in protocols:
            checking_handler(site, timeout, protocol, rand_UA)
    
    print()
    #print(f"|| {len(http_valid_proxies)} of {len(http_proxies)} ({http_percentage:.2f}%) HTTP proxies are currently active.")
    #print(f"|| {len(https_valid_proxies)} of {len(https_proxies)} ({https_percentage:.2f}%) HTTPS proxies are currently active.")

        print()
        banner()
        print(vanity_line)
        with suppress(Exception):
            print(f"|| {len(http_valid_proxies)} of {len(http_proxies)} ({http_percentage:.2f}%) HTTP proxies are currently active.")
        with suppress(Exception):
            print(f"|| {len(https_valid_proxies)} of {len(https_proxies)} ({https_percentage:.2f}%) HTTPS proxies are currently active.")
    exit_con()

def prox_check_handler(protocols, site, timeout):
    for protocol in protocols:
        checking_handler(site, timeout, protocol, rand_UA)

    print(vanity_line)
    print()
    input("Press enter to continue... ")
    banner()
    print(vanity_line)
    with suppress(Exception):
        print(f"|| {len(http_valid_proxies)} of {len(http_proxies)} ({http_percentage:.2f}%) HTTP proxies are currently active.")
    with suppress(Exception):
        print(f"|| {len(https_valid_proxies)} of {len(https_proxies)} ({https_percentage:.2f}%) HTTPS proxies are currently active.")

def exit_con():
    text = "||     Thank you for using proXXy.     ||"

    # Calculate the remaining empty space on the left and right
    empty_space = terminal_width - len(text)
    left_space = empty_space // 2
    right_space = empty_space - left_space

    print(vanity_line)
    print(" " * left_space + text + " " * right_space)
    print(vanity_line)
    exit()

def checking_handler(site, timeout, protocol, rand_UA):
    if protocol == "SOCKS4":
        with contextlib.suppress(Exception):
            SOCKS4_check(site, timeout, rand_UA)
    elif protocol == "SOCKS5":
        with contextlib.suppress(Exception):
            SOCKS5_check(site, timeout, rand_UA)
    elif protocol == "HTTP":
        with contextlib.suppress(Exception):
            HTTP_check(site, timeout, rand_UA)
    elif protocol == "HTTPS":
        with contextlib.suppress(Exception):
            HTTPS_check(site, timeout, rand_UA)

def init_main(error_log, site, timeout):
    try: 
        scraping_handler(error_log, site, timeout)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        exit_con()

def main():
    try:
        parameters()
        intro()
        warnings.filterwarnings("ignore", category=UserWarning, message=".*looks like you're parsing an XML document using an HTML parser.*")
        site = "http://httpbin.org/ip"
        # initialize files
        with open("scraped/HTTP.txt", "w"), open("scraped/SOCKS4.txt", "w"), open("scraped/SOCKS5.txt", "w"), open("scraped/HTTPS.txt", "w"), open("error.log", "w") as error_log:
            init_main(error_log, site, timeout)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        exit_con()

def run_update_script():
    current_os = platform.system()
    if (
        current_os == 'Linux'
        or current_os != 'Windows'
        and current_os == 'Darwin'
    ):
        # Change the permissions of the update script to make it executable
        subprocess.run(['chmod', '+x', 'update.sh'])
        # Run the update script
        subprocess.run(['./update.sh'])
    elif current_os == 'Windows':
        # Run the update batch script
        subprocess.run(['update.bat'])
    else:
        print('Unsupported operating system.')

    exit_con()

if __name__ == '__main__':
    global vanity_line
    global total_sources
    global accessed_sources

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', action='store_true', help='Run update script')
    args = parser.parse_args()

    terminal_width = shutil.get_terminal_size().columns

    dash = "—"
    dashes = dash * (terminal_width - 2)
    vanity_line = f"<{dashes}>"

    if args.u:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(vanity_line)
        run_update_script()

    total_sources = 0
    accessed_sources = 0
    main()
