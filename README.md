<a name="readme-top"></a>

<div align="center">

  [![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=200&size=98&duration=2000&pause=2000&color=831ACB&center=true&vCenter=true&width=1000&height=150&lines=————proXXy————)](https://git.io/typing-svg)

  <!-- BANNER -->
  <br />
  
 ---
***proXXy*** is a powerful tool designed for acquiring and managing a vast quantity of proxies. Its primary purpose is to gather, organize, and provide HTTP, SOCKS4, and SOCKS5 proxies. You can use them to do web scraping, penetration testing, bypassing censorship, simulated DDoS attacks, and more!

The software is currently capable of retrieving over 50,000 proxies from many different sources.

  This project is for educational purposes only— Please do not use this for illegal activities.
</div>

---

## Installation
-- Clone the repository:
```
git clone https://github.com/Atropa-Solanaceae/proXXy.git
```
-- Navigate to the project directory:
```
cd proXXy
```
-- Install the required dependencies:
```
pip3 install -r requirements.txt
```
## Usage
-- Run the program:
```
python3 proXXy.py
```
-- Select the execution parameters.

-- Allow the program to complete, then check the new text files located in `scraped/` directory!

The program will output three files in the project directory containing the regularized proxy lists: `HTTP.txt`, `SOCKS4.txt`, and `SOCKS5.txt`, along with an error output file titled `error.log` noting the links that were unable to be accessed.

## Update
To update the project, run:
```
python3 proXXy.py -u 
```

## Planned Features 
- Implement a feature for automatically testing the scraped proxies to verify their functionality. (1/3rd completed) 
- Proxy sorting instead of hardcoding.
- Provide an option to discern between Elite, Anonymous, and Transparent anonymity classes of proxies.

## Added Features
- HTTPS support.
- Easy updating!
- Added asynchronous webscraping.
- Fixed random user agents option.
- Added output folder for brevity.
- Added more user parameters.
- Verified proxies are written to checked file.
- Improve error handling and logging for more informative feedback to the user.
- Added a function to remove duplicate proxies from the generated lists.
- Added a function to regularize proxies by removing trash values.
- Updated the proxy scraping function to use contextlib.suppress for better error handling.

![img](https://github.com/Atropa-Solanaceae/proXXy/assets/89823371/d021ede8-5cb4-4ff6-bd77-2faf9a45ab83)

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.
