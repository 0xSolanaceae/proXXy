#!/usr/bin/python3
# Built by Solanaceae -- https://solanaceae.xyz/
import hrequests
from sys import argv
from re import findall
from random import choice
from subprocess import run
from os import name, system
from threading import Thread
from contextlib import suppress
from warnings import filterwarnings
from shutil import get_terminal_size
from pystyle import Colors, Colorate
from requests import get, exceptions
from platform import system as platform_system
from socket import timeout as socket_timeout
from argparse import ArgumentParser, ArgumentError, ArgumentTypeError


class NoneInputError(Exception):
    def __init__(self, message = "Error: No input was given. Please try again."):
        self.message = message
        super().__init__(self.message)


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
            "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt"
        ],
        "HTTPS": [
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
            "https://proxyspace.pro/https.txt",
            "https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt",
            "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
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

    system("title proXXy -- by Solanaceae")
    system('cls' if name == 'nt' else 'clear')
    print((Colorate.Vertical(Colors.purple_to_blue, banner, 1)))
    print()
    
def parameters():
    global timeout
    global prox_check
    global user_agents

    try:
        banner()
        prox_check_input = input("Would you like to check proxies? (Y/n): ").lower()
        if prox_check_input == "":
            raise NoneInputError()
        prox_check = prox_check_input.lower() != "n"
    except KeyboardInterrupt:
        exit_con()
    except NoneInputError:
        prox_check = True

    if prox_check:
        try:
            banner()
            timeout_input = input("How long should the request timeout be? (Default is 10 seconds, cannot be lower than 5): ")
            if timeout_input == "":
                raise NoneInputError()
            timeout_input = int(timeout_input)
            timeout = timeout_input if timeout_input >= 5 else 10
        except KeyboardInterrupt:
            exit_con()
        except NoneInputError:
            timeout = 10

        try:
            banner()
            threads_input = input("How many threads should be used? (Default is 100): ")
            if threads_input == "":
                raise NoneInputError()
            threads_input = int(threads_input)
        except KeyboardInterrupt:
            exit_con()
        except NoneInputError:
            threads = 100
    else:
        timeout = None
        threads = None
    

    user_agents = []
    with open("user_agents.txt", "r") as file:
        user_agents = file.read().splitlines()

    # Confirmation prompt
    banner()
    print(f"Selected options:\n")
    print(f" -- Proxy check: {prox_check}")
    if timeout is not None:
        print(f" -- Timeout: {timeout}")
    if threads is not None:
        print(f" -- Threads: {threads}")
    confirm_input = input("\nDo you want to continue? (Y/n): ").lower()
    # Check user's confirmation
    if confirm_input == "n":
        exit_con()
    main(timeout)

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
    proxies = findall(proxy_pattern, text_data)

    # Overwrite the original text document with the regularized proxies
    try:
        with open(f'scraped/{protocol}.txt', 'w') as file:
            file.write('\n'.join(lines)) #remove empty lines
            for proxy in proxies:
                file.write(proxy + '\n')

    except IOError:
        system('cls' if name == 'nt' else 'clear')
        print(vanity_line)
        print(f"\nError: Could not write to {protocol}.txt\n")
        exit_con()

## checking portion

def SOCKS4_check(site, timeout, threads):
    pass
    
def SOCKS5_check(site, timeout, threads):
    pass

def HTTP_check(site, timeout):
    from tqdm import tqdm
    global http_valid_proxies
    global http_proxies
    global http_percentage
    
    PROXY_LIST_FILE = 'scraped/HTTP.txt'
    TEST_URL = site
    TIMEOUT = timeout

    def test_proxy(proxy, results):
        with suppress(exceptions.RequestException, socket_timeout):
            headers = {}
            headers['User-Agent'] = choice(user_agents)
        
            response = get(TEST_URL, proxies={'http': proxy}, headers=headers, timeout=TIMEOUT)
            if response.status_code == 200:
                results.append(proxy)

    http_proxies = []
    http_valid_proxies = []
    with open(PROXY_LIST_FILE, 'r') as f:
        http_proxies = [line.strip() for line in f.readlines()]

    threads = []
    for proxy in tqdm(http_proxies, desc="Checking HTTP Proxies", ascii=" #", unit= " prox"):
        thread = Thread(target=test_proxy, args=(proxy, http_valid_proxies), daemon=True)
        threads.append(thread)
        thread.start()

    http_percentage = len(http_valid_proxies) / len(http_proxies) * 100

    for thread in threads: #tqdm(threads, desc="Joining Threads", ascii=" #", unit= " thr"):
        thread.join()

    with open(PROXY_LIST_FILE, 'w') as f:
        for proxy in http_valid_proxies:
            f.write(proxy + '\n')
    
def HTTPS_check(site, timeout):
    from tqdm import tqdm
    global https_valid_proxies
    global https_proxies
    global https_percentage
    
    PROXY_LIST_FILE = 'scraped/HTTPS.txt'
    TEST_URL = site
    TIMEOUT = timeout

    def test_proxy(proxy, results):
        with suppress(exceptions.RequestException, socket_timeout):
            headers = {}
            headers['User-Agent'] = choice(user_agents)

            response = get(TEST_URL, proxies={'https': proxy}, headers=headers, timeout=TIMEOUT)
            if response.status_code == 200:
                results.append(proxy)

    https_proxies = []
    https_valid_proxies = []
    with open(PROXY_LIST_FILE, 'r') as f:
        https_proxies = [line.strip() for line in f.readlines()]

    threads = []
    for proxy in tqdm(https_proxies, desc="Checking HTTPS Proxies", ascii=" #", unit= " prox"):
        thread = Thread(target=test_proxy, args=(proxy, https_valid_proxies), daemon=True)
        threads.append(thread)
        thread.start()

    https_percentage = len(https_valid_proxies) / len(https_proxies) * 100

    for thread in threads: #tqdm(threads, desc="Joining Threads", ascii=" #", unit= " thr"):
        thread.join()

    with open(PROXY_LIST_FILE, 'w') as f:
        for proxy in https_valid_proxies:
            f.write(proxy + '\n')

## proxy scraping

def scrape_url(url, proxy_type, error_log):
    global accessed_sources
    global total_sources

    total_sources += 1
    session = hrequests.Session()

    try:
        response = session.get(url)
        if response.status_code == 200:
            accessed_sources += 1
            scraped_data = response.html.text
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
        error_log.write(f" || Error message: {str(e)}\n")

def scraping_handler(error_log, site, timeout):
    from tqdm import tqdm
    global accessed_sources
    global total_sources

    print(vanity_line)

    # proxy sources
    proxies = proxy_sources()

    total_sources = 0
    accessed_sources = 0

    threads = []
    # webscraping proxies
    for proxy_type, urls in tqdm(proxies.items(), desc="Scraping Sources", ascii=" #", unit=" src"):
        for url in urls:
            thread = Thread(target=scrape_url, args=(url, proxy_type, error_log))
            thread.start()
            threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    print()

    if accessed_sources == 0:
        error = "|| A network error occured, please ensure your device is connected to the internet. ||"

        empty_space = terminal_width - len(error)
        left_space = empty_space // 2
        right_space = empty_space - left_space

        system('cls' if name == 'nt' else 'clear')
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
    for protocol in tqdm(protocols, desc="Regularizing Proxies", ascii=" #", unit= " prox"):
        regularize_proxies(protocol)
    for protocol in tqdm(protocols, desc="Removing Duplicates", ascii=" #", unit= " prox"):
        remove_duplicate_proxies(protocol)

    if prox_check:
        print()
        prox_check_handler(protocols, site, timeout)
    else:
        non_check_closure()

def non_check_closure():
    with (open("scraped/HTTP.txt", "r") as file_http, open("scraped/HTTPS.txt", "r") as file_https, open("scraped/SOCKS4.txt", "r") as file_socks4, open("scraped/SOCKS5.txt", "r") as file_socks5):
        http_scraped = len(file_http.readlines())
        https_scraped = len(file_https.readlines())
        socks4_scraped = len(file_socks4.readlines())
        socks5_scraped = len(file_socks5.readlines())
    print(vanity_line)
    print(f"|| {socks4_scraped:,} SOCKS4 proxies scraped.")
    print(f"|| {socks5_scraped:,} SOCKS5 proxies scraped.")
    print(f"|| {http_scraped:,} HTTP proxies scraped.")
    print(f"|| {https_scraped:,} HTTPS proxies scraped.")
    total = http_scraped + https_scraped + socks4_scraped + socks5_scraped
    print(f"|| Total proxies scraped: {total:,}.")

    text = "||     Thank you for using proXXy.     ||"

    # Calculate the remaining empty space on the left and right
    empty_space = terminal_width - len(text)
    left_space = empty_space // 2
    right_space = empty_space - left_space

    print(vanity_line)
    print(" " * left_space + text + " " * right_space)
    print(vanity_line)
    exit(1)
    
def prox_check_handler(protocols, site, timeout):
    global http_scraped, https_scraped, socks4_scraped, socks5_scraped
    with (open("scraped/HTTP.txt", "r") as file_http, open("scraped/HTTPS.txt", "r") as file_https, open("scraped/SOCKS4.txt", "r") as file_socks4, open("scraped/SOCKS5.txt", "r") as file_socks5):
        http_scraped = len(file_http.readlines())
        https_scraped = len(file_https.readlines())
        socks4_scraped = len(file_socks4.readlines())
        socks5_scraped = len(file_socks5.readlines())

    for protocol in protocols:
        checking_handler(choice(site), timeout, protocol)
    
    print(vanity_line)
    print()
    input("Press enter to continue... ")
    banner()
    print(vanity_line)
    print(f"|| {socks4_scraped:,} SOCKS4 proxies scraped.")
    print(f"|| {socks5_scraped:,} SOCKS5 proxies scraped.")
    print(f"|| {http_scraped:,} HTTP proxies scraped.")
    print(f"|| {https_scraped:,} HTTPS proxies scraped.")
    total = http_scraped + https_scraped + socks4_scraped + socks5_scraped
    print(f"|| {total:,} proxies scraped in total.")
    print(vanity_line)

    #with suppress(Exception):
    #    print(f"|| {len(socks5_valid_proxies)} of {len(socks5_proxies)} ({socks5_percentage:,:.2f}%) SOCKS5 proxies are currently active."
    #with suppress(Exception):
    #    print(f"|| {len(socks4_valid_proxies)} of {len(socks4_proxies)} ({socks4_percentage:,:.2f}%) SOCKS4 proxies are currently active.")
    with suppress(Exception):
        print(f"|| {len(http_valid_proxies):,} of {len(http_proxies):,} ({http_percentage:.2f}%) HTTP proxies are currently active.")
    with suppress(Exception):
        print(f"|| {len(https_valid_proxies):,} of {len(https_proxies):,} ({https_percentage:.2f}%) HTTPS proxies are currently active.")
    text = "||     Thank you for using proXXy.     ||"

    # Calculate the remaining empty space on the left and right
    empty_space = terminal_width - len(text)
    left_space = empty_space // 2
    right_space = empty_space - left_space

    print(vanity_line)
    print(" " * left_space + text + " " * right_space)
    print(vanity_line)
    exit(1)

def exit_con():
    text = "||     Thank you for using proXXy.     ||"

    # Calculate the remaining empty space on the left and right
    empty_space = terminal_width - len(text)
    left_space = empty_space // 2
    right_space = empty_space - left_space

    banner()
    print(vanity_line)
    print(" " * left_space + text + " " * right_space)
    print(vanity_line)
    exit(1)

def checking_handler(site, timeout, protocol):
    if protocol == "SOCKS4":
        with suppress(Exception):
            SOCKS4_check(site, timeout, threads=100)
    elif protocol == "SOCKS5":
        with suppress(Exception):
            SOCKS5_check(site, timeout, threads=100)
    elif protocol == "HTTP":
        with suppress(Exception):
            HTTP_check(site, timeout)
    elif protocol == "HTTPS":
        with suppress(Exception):
            HTTPS_check(site, timeout)

def main(timeout):
    try:
        banner()
        filterwarnings("ignore", category=UserWarning, message=".*looks like you're parsing an XML document using an HTML parser.*")
        site = ['http://httpbin.org/ip', 'https://httpbin.org/ip', 'http://example.com', 'https://example.com']
        # initialize files
        with open("scraped/HTTP.txt", "w"), open("scraped/SOCKS4.txt", "w"), open("scraped/SOCKS5.txt", "w"), open("scraped/HTTPS.txt", "w"), open("error.log", "w") as error_log:
            scraping_handler(error_log, site, timeout)
    except KeyboardInterrupt:
        system('cls' if name == 'nt' else 'clear')
        exit_con()

def run_update_script():
    current_os = platform_system()
    if (
        current_os == 'Linux'
        or current_os != 'Windows'
        and current_os == 'Darwin'
    ):
        # Change the permissions of the update script to make it executable
        run(['chmod', '+x', 'update.sh'])
        # Run the update script
        run(['./update.sh'])
    elif current_os == 'Windows':
        # Run the update batch script
        run(['update.bat'])
    else:
        print('Unsupported operating system.')

    exit_con()

def validate_positive_integer(value):
    ivalue = int(value)
    if ivalue < 1:
        raise ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue

def validate_timeout(value):
    ivalue = int(value)
    if ivalue < 5:
        raise ArgumentTypeError("Timeout cannot be lower than 5 seconds")
    return ivalue

if __name__ == '__main__':
    parser = ArgumentParser(description='A super simple multithreaded proxy scraper; scraping & checking ~80k HTTP, HTTPS, SOCKS4, & SOCKS5 proxies.')
    parser.add_argument('-u', '--update', action='store_true', help='update project')
    parser.add_argument('-v', '--validate', choices=['T', 'F'], help='validate proxies (T/F)')
    parser.add_argument('-th', '--threads', type=validate_positive_integer, default=100, help='number of threads to use, default is 100')
    parser.add_argument('-ti', '--timeout', type=validate_timeout, help='set the number of seconds for the default timeout (cannot be lower than 5 seconds)')
    parser.add_argument('-y', action='store_true', help='continue without prompts')

    args = parser.parse_args()

    terminal_width = get_terminal_size().columns
    dash = "—"
    dashes = dash * (terminal_width - 2)
    vanity_line = f"<{dashes}>"

    try:
        if len(argv) == 1:
            parameters()
        elif args.update:
            system('cls' if name == 'nt' else 'clear')
            print(vanity_line)
            run_update_script()
        else:
            prox_check = args.validate == 'T'
            if args.validate == 'T' and (args.threads is None or args.timeout is None):
                print("Error: If you use -vT, you must provide -th and -ti flags.")
                exit(1)

            if args.validate == 'T' and not args.y:
                print(vanity_line)
                print(f"Selected options:\n")
                print(f" -- Proxy check: {args.validate == 'T'}")
                print(f" -- Threads: {args.threads or 100}")
                print(f" -- Timeout: {args.timeout or 10}")
                print(vanity_line)
                confirm_input = input("\nDo you want to continue? (Y/n): ").lower()
                # Check user's confirmation
                if confirm_input == "n":
                    exit(1)
            main(args.timeout)
    except ArgumentError:
        parser.print_help()
    except KeyboardInterrupt:
        exit_con()
