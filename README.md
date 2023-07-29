<a name="readme-top"></a>

<div align="center">
  <p align="center">
    <a href="https://git.io/typing-svg">
      <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=200&size=98&duration=2000&pause=2000&color=831ACB&center=true&vCenter=true&width=1000&height=150&lines=\———\proXXy/———/" alt="Typing SVG" />
    </a>
  </p>
  
  <p align="center">
    <strong>proXXy</strong> is a powerful tool designed for acquiring and managing a vast quantity of proxies. Its primary purpose is to gather, organize, and provide HTTP, HTTPS, SOCKS4, and SOCKS5 proxies. They can be used for web scraping, penetration testing, bypassing censorship, DDoSing, and more!
  </p>
  
  <p align="center">
    The software is currently capable of retrieving over 50,000 proxies from many different sources.
  </p>
  
  <p align="center">
    This project is for educational purposes only— Please do not use this for illegal activities.
  </p>
</div>

---

## Installation

- Clone the repository:

```
git clone https://github.com/Atropa-Solanaceae/proXXy.git
```

- Navigate to the project directory:

```
cd proXXy
```

- Install the required dependencies:

```
pip3 install -r requirements.txt
```

## Simple Usage

- Run the program:

```
python3 proXXy.py
```

- Select the execution parameters.

- Allow the program to complete, then check the new text files located in `scraped/` directory! (After each instance of the checking process, allow the program time to join threads before moving on to the next proxy protocol.)

The program will output three files in the project directory containing the regularized proxy lists:

- `HTTP.txt`
- `HTTPS.txt`
- `SOCKS4.txt`
- `SOCKS5.txt`

along with an error output file titled `error.log` denoting the sources that were unable to be accessed.

## Advanced Usage

The basic syntax for running proXXy is as follows:

```
python3 proXXy.py [flags]
```

#### T/F = True/False (Boolean)

#### int = Integer

1. `-v[T/F], --validate`: Use this flag to enable proxy validation. The scraper will attempt to validate the scraped proxies by checking their accessibility.

2. `-r[T/F], --random-UA`: By including this flag, proXXy will use random user agents for each request, making it harder for servers to detect the scraper.

3. `-t[int], --timeout`: This flag allows you to set the default timeout for proXXy. The timeout specifies the number of seconds the scraper will wait for a response before considering a request as failed. The minimum timeout value is 10 seconds.

### Example

```
python3 proXXy.py -vT -rF -t10
```

4. `-y`: This flag allows you to skip the prompts and run proXXy with the given parameters. (Make sure you know what you're doing!)

### Example

```
python3 proXXy.py -vT -rF -t10 -y
```

5. `-u, --update`: This flag is used to update the project. When provided alone, it will trigger the update process, ensuring you have the latest version of proXXy.

6. `-h, --help`: Use this flag alone to display the help message that explains the available flags and their usage.

Remember to utilize the `-h` flag whenever you need a quick reference to the available flags and how to use them. The help message will be displayed as follows:

```
Usage: proXXy.py [-h] [-u] [-v {T,F}] [-r {T,F}] [-t TIMEOUT] [-y]

A super simple multithreaded proxy scraper; scraping & checking ~50k HTTP, HTTPS, SOCKS4, & SOCKS5 proxies.

options:
  -h, --help            show this help message and exit
  -u, --update          Update project
  -v {T,F}, --validate {T,F}
                        Validate proxies (T/F)
  -r {T,F}, --random-UA {T,F}
                        Use random user agents (T/F)
  -t TIMEOUT, --timeout TIMEOUT
                        Set the number of seconds for the default timeout (cannot be lower than 5 seconds) 
  -y                    Continue without prompts
```

## Notes

- The combination of flags `-v`, `-r`, and `-t` is allowed. However, if `-v` is set to "F" (disabled), the other flags `-r` and `-t` are not allowed.

- If you choose to enable proxy validation (`-v` flag), proXXy will display information about the total number of sources and the number of accessed sources after the validation process is completed.

- When using the `-u` flag to update the project, proXXy will clear the screen and show a status line indicating the update progress. The update process will take a few seconds to complete.

## Planned Features

- Implement a feature for automatically testing the scraped proxies to verify their functionality. (2/4th completed)
- Proxy sorting instead of hardcoding.
- Provide an option to discern between Elite, Anonymous, and Transparent anonymity classes of proxies.

## Support

Need help and can't get it to run correctly? Open an issue or contact me [here](https://solanaceae.xyz/)

---

![img](https://github.com/Atropa-Solanaceae/proXXy/assets/89823371/193b1828-bc9f-4c99-8f6a-f16238e9a888)

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
