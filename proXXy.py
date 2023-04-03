#!/usr/bin/python3
#Coded by Solanaceae
import contextlib
import requests
import os
import warnings
import re
from bs4 import BeautifulSoup
from pystyle import *

warnings.filterwarnings("ignore", category=UserWarning, message=".*looks like you're parsing an XML document using an HTML parser.*")

S = r"""
 ▄████████  ▄██████▄   ▄█          ▄████████ ███▄▄▄▄      ▄████████  ▄████████    ▄████████    ▄████████    ▄████████ 
  ███    ███ ███    ███ ███         ███    ███ ███▀▀▀██▄   ███    ███ ███    ███   ███    ███   ███    ███   ███    ███ 
  ███    █▀  ███    ███ ███         ███    ███ ███   ███   ███    ███ ███    █▀    ███    █▀    ███    ███   ███    █▀  
  ███        ███    ███ ███         ███    ███ ███   ███   ███    ███ ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄     
▀███████████ ███    ███ ███       ▀███████████ ███   ███ ▀███████████ ███        ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀     
         ███ ███    ███ ███         ███    ███ ███   ███   ███    ███ ███    █▄    ███    █▄    ███    ███   ███    █▄  
   ▄█    ███ ███    ███ ███▌    ▄   ███    ███ ███   ███   ███    ███ ███    ███   ███    ███   ███    ███   ███    ███ 
 ▄████████▀   ▀██████▀  █████▄▄██   ███    █▀   ▀█   █▀    ███    █▀  ████████▀    ██████████   ███    █▀    ██████████ """

os.system("title proXXy")
os.system('cls' if os.name == 'nt' else 'clear')
print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue, S, 1)))
print("<---------------------------------------------------------------------------------------------------------------------->")
print("")

import tqdm

def process_proxies(protocol):
    # Read in the text document
    try:
        with open(f'{protocol}.txt', 'r') as file:
            proxies_data = file.read()
    except IOError:
        print(f"Error: Could not read {protocol}.txt")
        return

    # Split the proxies into a list and remove duplicates
    proxies = proxies_data.splitlines()
    unique_proxies = list(set(proxies))

    # Overwrite the original text document with the unique proxies
    try:
        with open(f'{protocol}.txt', 'w') as file:
            for proxy in tqdm.tqdm(unique_proxies, desc=f"Removing Duplicates in {protocol}", ascii=" #", unit= " prox"):
                file.write(proxy + '\n')
    except IOError:
        print(f"Error: Could not write to {protocol}.txt")
        return
    
def regularize_proxies(protocol):
    try:
        with open(f'{protocol}.txt', 'r') as file:
            text_data = file.read()
    except IOError:
        print(f"Error: Could not read {protocol}.txt")
        return

    # Define a regex pattern to match proxies
    proxy_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+'
    proxies = re.findall(proxy_pattern, text_data)

    # Overwrite the original text document with the regularized proxies
    try:
        with open(f'{protocol}.txt', 'w') as file:
            for proxy in tqdm.tqdm(proxies, desc=f"Regularizing {protocol}", ascii=" #", unit= " prox"):
                file.write(proxy + '\n')
    except IOError:
        print(f"Error: Could not write to {protocol}.txt")
        return

def main():
    # initialize files
    with (open("http.txt", "w") as file_http, open("socks4.txt", "w") as file_socks4, open("socks5.txt", "w") as file_socks5):

        # proxy sources
        proxies = {
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
                "https://raw.githubusercontent.com/RX4096/proxy-list/main/online/all.txt",
                "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
                "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
                "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
                "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
                "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
                "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
                "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
                "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
                "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt",
                "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
                "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt",
                "https://raw.githubusercontent.com/BlackSnowDot/proxylist-update-every-minute/main/https.txt",
                "https://raw.githubusercontent.com/BlackSnowDot/proxylist-update-every-minute/main/http.txt",
                "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
                "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                "http://rootjazz.com/proxies/proxies.txt",
                "http://spys.me/proxy.txt",
                "https://sheesh.rip/http.txt",
                "http://worm.rip/http.txt",
                "http://www.proxyserverlist24.top/feeds/posts/default",
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
                "https://www.freeproxychecker.com/result/http_proxies.txt",
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
                "https://www.freeproxychecker.com/result/socks4_proxies.txt",
                "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt",
                "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
                "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
                "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
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
                "https://raw.githubusercontent.com/BlackSnowDot/proxylist-update-every-minute/main/socks.txt",
                "http://worm.rip/socks5.txt",
                "http://www.socks24.org/feeds/posts/default",
                "https://www.freeproxychecker.com/result/socks5_proxies.txt",
                "https://www.proxy-list.download/api/v1/get?type=socks5",
                "https://www.proxyscan.io/download?type=socks5",
                "https://www.my-proxy.com/free-socks-5-proxy.html",
            ]
        }

        total_links = 0
        accessed_links = 0

        # webscraping proxies
        for proxy_type, urls in proxies.items():
            for url in tqdm.tqdm(urls, desc=f"Scraping {proxy_type}", ascii=" #", unit= " prox"):
                with contextlib.suppress(requests.exceptions.RequestException):
                    response = requests.get(url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.content, 'html.parser')
                        scraped_data = soup.get_text()
                        if proxy_type == "HTTP":
                            with open("http.txt", "a") as file_http:
                                file_http.write(scraped_data + '\n')
                        elif proxy_type == "SOCKS4":
                            with open("socks4.txt", "a") as file_socks4:
                                file_socks4.write(scraped_data + '\n')
                        elif proxy_type == "SOCKS5":
                            with open("socks5.txt", "a") as file_socks5:
                                file_socks5.write(scraped_data + '\n')
                        accessed_links += 1
                total_links += 1


        print("")
        print(f"Total Links: {total_links}")
        print(f"Accessed Links: {accessed_links}")
        print("")

        protocols = ["HTTP", "SOCKS4", "SOCKS5"]
        for protocol in protocols:
            regularize_proxies(protocol)
        print("")

        for protocol in protocols:
            process_proxies(protocol)
        print("")

        print("Process completed!")
        print("<---------------------------------------------------------------------------------------------------------------------->")


if __name__ == '__main__':
    main()
