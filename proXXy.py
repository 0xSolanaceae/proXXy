#!/usr/bin/python3
#Coded by Solanaceae
import os
import re
import socket
import random
import threading
import requests
import warnings
import contextlib
from bs4 import BeautifulSoup
from pystyle import *

def parameters():
    global rand_UA
    global timeout
    global prox_check

    rand_UA = False
    '''try:
        intro()
        rand_UA_input = input("Would you like to use random user agents? (Y/n): ").lower()
        if rand_UA_input == "":
            raise Exception
        rand_UA = rand_UA_input.lower() != "n"
    except Exception:
        rand_UA = True'''

    try:
        intro()
        timeout_input = input("How long should the request timeout be? (Default is 10 seconds): ")
        if timeout_input == "":
            raise Exception
        timeout_input = int(timeout_input)
        timeout = timeout_input if timeout_input > 0 else 10
    except Exception:
        timeout = 10

    try:
        intro()
        prox_check_input = input("Would you like to check HTTP proxies? (Y/n): ").lower()
        if prox_check_input == "":
            raise Exception
        prox_check = prox_check_input.lower() != "n"
    except Exception:
        prox_check = True


    # Confirmation prompt
    intro()
    print(f"Selected options:\n\n -- Random user agents: {rand_UA}\n -- Timeout: {timeout}\n -- Proxy check: {prox_check}")
    confirm_input = input("\nDo you want to continue with these options? (Y/n): ").lower()

    # Check user's confirmation
    if confirm_input == "n":
        parameters()

def intro(): 
    S = r"""
 ▄████████  ▄██████▄   ▄█          ▄████████ ███▄▄▄▄      ▄████████  ▄████████    ▄████████    ▄████████    ▄████████ 
  ███    ███ ███    ███ ███         ███    ███ ███▀▀▀██▄   ███    ███ ███    ███   ███    ███   ███    ███   ███    ███ 
  ███    █▀  ███    ███ ███         ███    ███ ███   ███   ███    ███ ███    █▀    ███    █▀    ███    ███   ███    █▀  
  ███        ███    ███ ███         ███    ███ ███   ███   ███    ███ ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄     
▀███████████ ███    ███ ███       ▀███████████ ███   ███ ▀███████████ ███        ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀     
         ███ ███    ███ ███         ███    ███ ███   ███   ███    ███ ███    █▄    ███    █▄    ███    ███   ███    █▄  
   ▄█    ███ ███    ███ ███▌    ▄   ███    ███ ███   ███   ███    ███ ███    ███   ███    ███   ███    ███   ███    ███ 
 ▄████████▀   ▀██████▀  █████▄▄██   ███    █▀   ▀█   █▀    ███    █▀  ████████▀    ██████████   ███    █▀    ██████████ """

    os.system("title proXXy -- by Solanaceae")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue, S, 1)))
    print("")
    print("<——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————>")

def proxy_sources():
    return {
        "HTTP": [
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt",
            "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
            "https://api.openproxylist.xyz/http.txt",
            "http://alexa.lr2b.com/proxylist.txt",
            "https://multiproxy.org/txt_all/proxy.txt",
            "https://proxyspace.pro/http.txt",
            "https://proxyspace.pro/https.txt",
            "https://proxy-spider.com/api/proxies.example.txt",
            "http://proxysearcher.sourceforge.net/Proxy%20List.php?type=http",
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
            "http://worm.rip/http.txt",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://www.proxyscan.io/download?type=http",
            "https://www.my-proxy.com/free-anonymous-proxy.html",
            "https://www.my-proxy.com/free-transparent-proxy.html",
            "https://www.my-proxy.com/free-proxy-list.html",
            "https://www.my-proxy.com/free-proxy-list-2.html",
            "https://www.my-proxy.com/free-proxy-list-3.html",
            "https://www.my-proxy.com/free-proxy-list-4.html",
            "https://www.my-proxy.com/free-proxy-list-5.html",
            "https://www.my-proxy.com/free-proxy-list-6.html",
            "https://www.my-proxy.com/free-proxy-list-7.html",
            "https://www.my-proxy.com/free-proxy-list-8.html",
            "https://www.my-proxy.com/free-proxy-list-9.html",
            "https://www.my-proxy.com/free-proxy-list-10.html",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt",
            "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
            "https://sunny9577.github.io/proxy-scraper/proxies.txt",
            "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt", # good one
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
            "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
        ],
        "SOCKS4": [
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4",
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4",
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
            "https://api.openproxylist.xyz/socks4.txt",
            "https://proxyspace.pro/socks4.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
            "http://worm.rip/socks4.txt",
            "https://www.proxy-list.download/api/v1/get?type=socks4",
            "https://www.proxyscan.io/download?type=socks4",
            "https://www.my-proxy.com/free-socks-4-proxy.html",
            "http://www.socks24.org/feeds/posts/default",
            "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks4.txt",
            "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt",
            "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt", # good one
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",
            "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt",
            "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt",
        ],
        "SOCKS5": [
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
            "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt",
            "https://api.openproxylist.xyz/socks5.txt",
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5",
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5",
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",
            "https://proxyspace.pro/socks5.txt",
            "https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
            "http://worm.rip/socks5.txt",
            "http://www.socks24.org/feeds/posts/default",
            "https://www.proxy-list.download/api/v1/get?type=socks5",
            "https://www.proxyscan.io/download?type=socks5",
            "https://www.my-proxy.com/free-socks-5-proxy.html",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks5.txt",
            "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt",
            "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt", # good one
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
            "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt",
            "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt",
        ],
        #"HTTPS": [ # not implemented yet
        #    "http://sslproxies.org",
        #    "https://github.com/jetkai/proxy-list/blob/main/online-proxies/txt/proxies-https.txt",
        #    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
        #]
    }

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
    except IOError:
        print(f"Error: Could not read {protocol}.txt")
        return

    # Define a regex pattern to match proxies
    proxy_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+'
    proxies = re.findall(proxy_pattern, text_data)

    # Overwrite the original text document with the regularized proxies
    try:
        with open(f'scraped/{protocol}.txt', 'w') as file:
            for proxy in proxies:
                file.write(proxy + '\n')
    except IOError:
        print(f"Error: Could not write to {protocol}.txt")
        return

def checking_handler(site, timeout, protocol, rand_UA):
    if protocol == "HTTP":
        HTTP_check(site, timeout, rand_UA)
    elif protocol in ["SOCKS4", "SOCKS5"]:
        return # temp response TODO

def HTTP_check(site, timeout, rand_UA):
    import tqdm
    PROXY_LIST_FILE = 'scraped/HTTP.txt'
    TEST_URL = site
    TIMEOUT = timeout
    def test_proxy(proxy, results):
        with contextlib.suppress(requests.exceptions.RequestException, socket.timeout):
            response = requests.get(TEST_URL, proxies={'http': proxy}, timeout=TIMEOUT)
            if response.status_code == 200:
                results.append(proxy)

    proxies = []
    valid_proxies = []
    with open(PROXY_LIST_FILE, 'r') as f:
        proxies = [line.strip() for line in f.readlines()]

    threads = []
    for proxy in tqdm.tqdm(proxies, desc="Checking proxies", ascii=" #", unit= " prox"):
        thread = threading.Thread(target=test_proxy, args=(proxy, valid_proxies), daemon=True)
        threads.append(thread)
        thread.start()

    for thread in tqdm.tqdm(threads, desc="Joining threads", ascii=" #", unit= " prox"):
        thread.join()

    with open(PROXY_LIST_FILE, 'w') as f:
        for proxy in valid_proxies:
            f.write(proxy + '\n')

    percentage = len(valid_proxies) / len(proxies) * 100
    print(f"All done! {len(valid_proxies)} of {len(proxies)} ({percentage:.2f}%) HTTP proxies are currently active.")

def SOCKS4_check():
    pass

def SOCKS5_check():
    pass

def scraping_handler(error_log, site, timeout):
    import tqdm
    # proxy sources
    proxies = proxy_sources()

    total_links = 0
    accessed_links = 0

    # webscraping proxies
    for proxy_type, urls in proxies.items():
        for url in tqdm.tqdm(urls, desc=f"Scraping {proxy_type}", ascii=" #", unit= " src"):
            with contextlib.suppress(requests.exceptions.RequestException):
                response = requests.get(url)
                if response.status_code == 200:
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
                    accessed_links += 1
                else:
                    error_log.write(f"Could not access: {url}\n")
            total_links += 1


    print("")
    print(f"Total Links: {total_links} || Accessed Links: {accessed_links}")
    print("")

    if accessed_links == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("<——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————>")
        print("\n                     A network error occured, please ensure your device is connected to the internet                \n")
        exit_con()

    protocols = ["HTTP", "SOCKS4", "SOCKS5"]
    for protocol in tqdm.tqdm(protocols, desc="Regularizing Proxies", ascii=" #", unit= " prox"):
        regularize_proxies(protocol)
    for protocol in tqdm.tqdm(protocols, desc="Removing Duplicates", ascii=" #", unit= " prox"):
        remove_duplicate_proxies(protocol)
    print("")
    
    if prox_check == True:
        for protocol in protocols:
            checking_handler(site, timeout, protocol, rand_UA)
    print("<——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————>")

def init_main(error_log, site, timeout):
    try: 
        scraping_handler(error_log, site, timeout)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        exit_con()

def exit_con():
    print("<——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————>")
    print("                                     ||     Thank you for using proXXy.     ||                                          ")
    print("<——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————>")
    exit()

def main():
    try:
        parameters()
        intro()
        warnings.filterwarnings("ignore", category=UserWarning, message=".*looks like you're parsing an XML document using an HTML parser.*")
        site = "http://httpbin.org/ip"
        # initialize files
        with open("scraped/HTTP.txt", "w"), open("scraped/SOCKS4.txt", "w"), open("scraped/SOCKS5.txt", "w"), open("error.log", "w") as error_log:
            init_main(error_log, site, timeout)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        exit_con()
        
if __name__ == '__main__':
    main()
