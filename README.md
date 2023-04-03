# ProXXy

ProXXy is a tool for scraping and regularizing proxy lists. It can be used to collect and organize lists of HTTP, SOCKS4, and SOCKS5 proxies for use in web scraping, data mining, and other tasks.

## Installation

To install ProXXy, follow these steps:

1. Clone the repository: `git clone https://github.com/Atropa-Solanaceae/proXXy.git`
2. Navigate to the project directory: `cd proXXy`
3. Install the required dependencies: `pip3 install -r requirements.txt`

## Usage

To use ProXXy, follow these steps:

1. Place any text files containing proxy lists in the project directory.
2. Run the program: `python3 proXXy.py`
3. Follow the prompts to select the type of proxies to scrape and regularize.

The program will output three files in the project directory containing the regularized proxy lists: `http.txt`, `socks4.txt`, and `socks5.txt`.

## Planned Features
- Implement a feature for automatically testing the scraped proxies to verify their functionality.
- Improve error handling and logging for more informative feedback to the user.
- Add support for HTTPS proxies.

## Added Features
- Added a function to remove duplicate proxies from the generated lists.
- Added a function to regularize proxies by removing trash values.
- Updated the proxy scraping function to use contextlib.suppress for better error handling.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.


![image](https://user-images.githubusercontent.com/89823371/229643010-7eff1a16-b10e-4b98-a50b-15495582903e.png)

