# ProXXy

ProXXy is a tool for scraping and regularizing proxy lists. It can be used to collect and organize lists of HTTP, SOCKS4, and SOCKS5 proxies for use in web scraping, data mining, *simulated* DDoS attacks, and other tasks. Currently finds more than 100k proxies from ~100 different sources.

## Installation

To install ProXXy, follow these steps:

1. Clone the repository: `git clone https://github.com/Atropa-Solanaceae/proXXy.git`
2. Navigate to the project directory: `cd proXXy`
3. Install the required dependencies: `pip3 install -r requirements.txt`

## Usage

To use ProXXy, follow these steps:

1. Ensure all files are within the same directory.
2. Run the program: `python3 proXXy.py`
3. Decide whether you want random user agents per each proxy request (may take longer, however it's more anonymous)
4. Allow the program to complete, then check the new text files!

The program will output three files in the project directory containing the regularized proxy lists: `HTTP.txt`, `SOCKS4.txt`, and `SOCKS5.txt`, along with an error logging file named `error.log` to assist you in debugging.

## Planned Features 
`Proxy checking is in Beta Testing`
- Implement a feature for automatically testing the scraped proxies to verify their functionality. (1/3rd completed) 
- Proxy Sorting instead of hardcoding.
- Provide an option to discern between Elite, Anonymous, and Transparent anonymity classes of proxies.
- Add support for HTTPS proxies.

## Added Features
- Added option to choose random user agents with every proxy request.
- Verified proxies are written to checked file.
- Improve error handling and logging for more informative feedback to the user.
- Added a function to remove duplicate proxies from the generated lists.
- Added a function to regularize proxies by removing trash values.
- Updated the proxy scraping function to use contextlib.suppress for better error handling.

## Disclaimer
This project is for educational purposes only— Please do not use this for illegal activities.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

![img](https://user-images.githubusercontent.com/89823371/231321673-0b8312c7-0cb2-4ca9-af42-bddf706fa1af.png)

