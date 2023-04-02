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

import tqdm

# initialize files
file_http = open("http.txt", "w")
file_socks4 = open("socks4.txt", "w")
file_socks5 = open("socks5.txt", "w")

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

http_proxies = ""
socks4_proxies = ""
socks5_proxies = ""

total_links = 0
accessed_links = 0

# webscraping proxies
for proxy_type, urls in proxies.items():
    print(f"\nScraping Proxy Type: {proxy_type}")
    for url in tqdm.tqdm(urls):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            scraped_data = soup.get_text()
            if proxy_type == "HTTP":
                http_proxies += scraped_data
                file_http = open("http.txt", "a")
                file_http.write(http_proxies)
            elif proxy_type == "SOCKS4":
                socks4_proxies += scraped_data
                file_socks4 = open("socks4.txt", "a")
                file_socks4.write(socks4_proxies)
            elif proxy_type == "SOCKS5":
                socks5_proxies += scraped_data
                file_socks5 = open("socks5.txt", "a")
                file_socks5.write(socks5_proxies)
                
            accessed_links += 1
        except TimeoutError as e:
            print(f"  Error: {url} returned a status code of {response.status_code}", e)
        total_links += 1


print("")
print(f"Total Links: {total_links}")
print(f"Accessed Links: {accessed_links}")
print("")

def ProxyProcessing(protocol):
    with open(f'{protocol}.txt', 'r') as f:
        proxies = f.read().splitlines()

    # remove duplicates from the list
    unique_proxies = list(set(proxies))

    # write the unique proxies back to the file
    with open(f'{protocol}.txt', 'w') as f:
        for proxy in unique_proxies:
            f.write(proxy + '\n')

def ProxyRegularizing(protocol):
    # read in the text document
    with open(f'{protocol}.txt', 'r') as file:
        text = file.read()

    # define a regex pattern to match proxies
    proxy_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+'
    proxies = re.findall(proxy_pattern, text)

    with open(f'{protocol}.txt', 'w') as file:
        for proxy in proxies:
            file.write(proxy + '\n')

         
protocols = ["http", "socks4", "socks5"]
for protocol in tqdm.tqdm(protocols, desc="Regularizing"):
    ProxyRegularizing(protocol)

for protocol in tqdm.tqdm(protocols, desc="Removing Duplicates"):
    ProxyProcessing(protocol)

print("\nProcess completed!\n")
file_http.close()
file_socks4.close()
file_socks5.close()