<a name="readme-top"></a>

<div align="center">

  [![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=200&size=98&duration=2000&pause=2000&color=831ACB&center=true&vCenter=true&width=1000&height=150&lines=%3C%7C---proXXy---%7C%3E)](https://git.io/typing-svg)

  <!-- BANNER -->
  <br />
  
 ---
***proXXy*** is a powerful tool designed for acquiring and managing a vast quantity of proxies. Its primary purpose is to gather and organize HTTP, SOCKS4, and SOCKS5 proxies, making them ideal for various tasks, such as web scraping, web penetration testing, censorship bypassing, DDoSing, and other similar activities. 

The software is currently capable of retrieving over 100,000 proxies from approximately 100 different sources.

  This project is for educational purposes only— Please do not use this for illegal activities.
</div>

---

## Installation

To install proXXy, follow these steps:

Clone the repository:
```
git clone https://github.com/Atropa-Solanaceae/proXXy.git
```
Navigate to the project directory:
```
cd proXXy
```
Install the required dependencies:
```
pip3 install -r requirements.txt
```
## Usage

1. Ensure all files are within the same directory.
2. Run the program:
```
python3 proXXy.py
```
3. Select the execution parameters.
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

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

![img](https://user-images.githubusercontent.com/89823371/231321673-0b8312c7-0cb2-4ca9-af42-bddf706fa1af.png)

