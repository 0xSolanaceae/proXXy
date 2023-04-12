#!/usr/bin/python3 
#Coded by Solanaceae
import os
import re
import socks
import socket
import random
import asyncio
import requests
import warnings
import contextlib
from bs4 import BeautifulSoup
from pystyle import *

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
    print("<---------------------------------------------------------------------------------------------------------------------->")

os.system('cls' if os.name == 'nt' else 'clear')
global rand_UA
try:
    intro()
    rand_UA = input("Would you like to use random user agents? (Y/n): ")
    rand_UA = rand_UA.lower() != "n"
except Exception:
    rand_UA = True

intro()
import tqdm

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
            "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt", # good one
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
            for proxy in unique_proxies:
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
            for proxy in proxies:
                file.write(proxy + '\n')
    except IOError:
        print(f"Error: Could not write to {protocol}.txt")
        return

def checking_handler(proxy_file, site, timeout, protocol, rand_UA):
    if protocol == "HTTP":
        return # temp response TODO
    elif protocol == "SOCKS4":
        SOCKS4_check(proxy_file, site, timeout, rand_UA)
    elif protocol == "SOCKS5":
        return # temp response TODO

def SOCKS4_check(proxy_file, site, timeout, rand_UA):
    # Set up the SOCKS4 proxy
    def set_proxy(ip, port):
        socks.set_default_proxy(socks.SOCKS4, ip, port)
        socket.socket = socks.socksocket

    # Read the user agents from the file
    with open("user_agents.txt", "r") as f:
        user_agents = [line.strip() for line in f.readlines()]

    # Function to get a random user agent
    def get_random_user_agent():
        return random.choice(user_agents)

    async def check_proxy(proxy, valid_proxies, rand_UA):
        with contextlib.suppress(Exception):
            ip, port = proxy.split(":")
            set_proxy(ip, int(port))
            
            headers = {}
            if rand_UA:
                headers["User-Agent"] = get_random_user_agent()
                
            reader, writer = await asyncio.open_connection(site, 80, limit=timeout)
            writer.write(b"GET / HTTP/1.1\r\n")
            for header, value in headers.items():
                writer.write(f"{header}: {value}\r\n".encode("utf-8"))
            writer.write(b"\r\n")
            writer.close()
            await writer.wait_closed()
            valid_proxies.append(proxy)

    # Read the proxy list from the file
    with open(proxy_file, "r") as f:
        proxies = [line.strip() for line in f.readlines()]

    # Set up the event loop and run the checks
    async def main():
        valid_proxies = []
        tasks = []
        with tqdm.tqdm(total=len(proxies), desc="Checking SOCKS4", ascii=" #", unit="prox") as pbar:
            for proxy in proxies:
                task = asyncio.create_task(check_proxy(proxy, valid_proxies, rand_UA))
                task.add_done_callback(lambda _: pbar.update())
                tasks.append(task)
            await asyncio.gather(*tasks)

        percentage = len(valid_proxies) / len(proxies) * 100
        print(f"Checked! {len(valid_proxies)} of {len(proxies)} ({percentage:.2f}%) SOCKS4 proxies are currently active.")
        # Write the verified proxies back to the SOCKS4.txt file
        with open(proxy_file, "w") as f:
            f.write("\n".join(valid_proxies))

    asyncio.run(main())


def SOCKS5_check(proxy_file, site, timeout):
    pass

def init_main(error_log, site, timeout):
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
                        with open("HTTP.txt", "a") as file_http:
                            file_http.write(scraped_data + '\n')
                    elif proxy_type == "SOCKS4":
                        with open("SOCKS4.txt", "a") as file_socks4:
                            file_socks4.write(scraped_data + '\n')
                    elif proxy_type == "SOCKS5":
                        with open("SOCKS5.txt", "a") as file_socks5:
                            file_socks5.write(scraped_data + '\n')
                    accessed_links += 1
                else:
                    error_log.write(f"Could not access: {url}\n")
            total_links += 1


    print("")
    print(f"Total Links: {total_links} || Accessed Links: {accessed_links}")
    print("")

    protocols = ["HTTP", "SOCKS4", "SOCKS5"]
    for protocol in tqdm.tqdm(protocols, desc="Regularizing Proxies", ascii=" #", unit= " prox"):
        regularize_proxies(protocol)
    for protocol in tqdm.tqdm(protocols, desc="Removing Duplicates", ascii=" #", unit= " prox"):
        remove_duplicate_proxies(protocol)
    print("")

    for protocol in protocols:
        checking_handler(f"{protocol}.txt", site, timeout, protocol, rand_UA)
    #SOCKS4_check("SOCKS4.txt", site, 2)
    print("<---------------------------------------------------------------------------------------------------------------------->")

def main():
    warnings.filterwarnings("ignore", category=UserWarning, message=".*looks like you're parsing an XML document using an HTML parser.*")
    site = "www.icanhazip.com"
    timeout = 10 
    # initialize files
    with (open("HTTP.txt", "w") as file_http, open("SOCKS4.txt", "w") as file_socks4, open("SOCKS5.txt", "w") as file_socks5, open("error.log", "w") as error_log):
        init_main(error_log, site, timeout)
        
if __name__ == '__main__':
    main()
