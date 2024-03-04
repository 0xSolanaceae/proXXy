<a name="readme-top"></a>

<div align="center">
  <p align="center">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=200&size=70&duration=2000&pause=2000&color=946df7&center=true&vCenter=true&width=1000&height=150&lines=<|———|> proXXy <|———|>" alt="proXXy typing out"/>
  </p>
  
  <p align="center">
    <strong>proXXy</strong> is a powerful tool designed for acquiring and managing a vast quantity of proxies. It is used to gather, organize, and procure HTTP/S, SOCKS4, and SOCKS5 proxies. They can be used for web scraping, penetration testing, bypassing censorship, and many other tasks!
  </p>
  
  <p align="center">
    The software is currently capable of retrieving over 500,000 proxies from many different sources.
  </p>
  
  <p align="center">
    This project is for educational purposes only— Please do not use this for illegal activities.
  </p>
</div>

---

## Installation

- Clone the repository:

```bash
git clone https://github.com/Atropa-Solanaceae/proXXy.git
```

- Navigate to the project directory:

```bash
cd proXXy
```

- Install the required dependencies:

```bash
pip3 install -r requirements.txt
```

## Usage

- Running the program without flags results in only scraping, as checking is disabled by default.

```python
python3 proXXy.py
```

The program will output four files in the project directory containing the regularized proxy lists:

- `HTTP.txt`
- `HTTPS.txt`
- `SOCKS4.txt`
- `SOCKS5.txt`

along with an error output file titled `error.log` denoting the sources that were unable to be accessed.
## Flags

The basic syntax for running proXXy is as follows:

```python
usage: proXXy.py [-h] [--validate] [--update] [--version]
```

1. `-v, --validate`: Use this flag to enable proxy validation. The scraper will attempt to validate the scraped proxies by checking their accessibility. Allow the program to complete the checking of HTTP & HTTPS proxies, then check the updated text files located in `output/` directory! (Please allow for up to 10 minutes for proxies to validate, depending on your hardware.)

2. `-u, --update`: This flag updates the project. Cannot be used in conjunction with any other flag.

3. `-h, --help`: Use this flag to spit out a help menu.

4. `-V, --version`: Use this flag to spit out `proXXy.py`'s version.

```bash
usage: proXXy.py [-h] [--validate] [--update] [--version]

A super simple multithreaded proxy scraper; scraping & checking ~500k HTTP, HTTPS, SOCKS4 & SOCKS5 proxies.

options:
  -h, --help      show this help message and exit
  --validate, -v  Flag to validate proxies after scraping (default: False)
  --update, -u    Flag to run the update script and then exit
  --version, -V   Print the version of the script and exit
```

## Planned Features

- Allow the user to choose the number of threads they'd like to use with flags, & provide the user recommended values based on their hardware.
- Implement SOCKS4 & SOCKS5 testing.
- Proxy sorting instead of hardcoding.
- Discerning between Elite, Anonymous, and Transparent anonymity classes of proxies.

## Support

Need help and can't get it to run correctly? Open an issue or contact me [here](https://solanaceae.xyz/).

## Changelog

[Release v2.2](https://github.com/Atropa-Solanaceae/proXXy/releases/tag/v2.2)
- Added a `--version, -V` flag
- Segmented resources into seperate files
- Further modularized code, more to come shortly 


---
## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
