<a name="readme-top"></a>

<div align="center">
  <p align="center">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=70&duration=2000&pause=1000&color=946DF7&center=true&width=1000&height=150&lines=%3C%7C%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94+proXXy+%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%7C%3E" alt="Typing SVG" /></a>
  
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
git clone https://github.com/0xSolanaceae/proXXy.git
cd proXXy
```

- Install dependencies (pip or poetry):

```bash
pip install -r requirements.txt
# or
poetry install
```

## Usage

- (Optional) activate the poetry shell:

```bash
poetry shell
```

- Run the scraper (validation is opt-in via `-V`):

```bash
python proXXy.py
```

The program will modify four files in the `output/` directory with your proxies:

- `HTTP.txt`
- `HTTPS.txt`
- `SOCKS4.txt`
- `SOCKS5.txt`

 with a logfile (`error.log`) with warnings/errors.

### Benchmarking the validator

The async validator can be micro-benchmarked against your network limits:

```bash
python benchmarks/bench_validate.py --concurrency 80 --timeout 5 --repeat 3 --limit 5 --quiet
```

Use `--limit` to cap URLs per protocol when you just want quick measurements.

## Flags

Syntax for running proXXy is as follows:

```bash
usage: proXXy.py [-h] [--validate] [--update] [--version] [--src_check]
```

1. `-V, --validate`: This flag enables proxy validation. The scraper will look to validate the scraped proxies by checking their accessibility.

2. `-u, --update`: This flag updates the project. Cannot be used in conjunction with any other flag.

3. `-h, --help`: Use this flag to spit out a help menu.

4. `-v, --version`: Use this flag to spit out `proXXy.py`'s version.

5. `-s, --src_check`: Use this flag to categorize the sources according to how many proxies they provide.

```bash
usage: proXXy.py [-h] [--validate] [--update] [--version] [--src_check]

A super simple asynchronous multithreaded proxy scraper;
scraping & checking ~500k HTTP, HTTPS, SOCKS4, & SOCKS5 proxies.

options:
  -h, --help      show this help message and exit
  --validate, -v  Flag to validate proxies after scraping (default: False)
  --update, -u    Flag to run the update script and then exit
  --version, -V   Print the version of the script and exit
  --src_check, -s Flag to verify sources
```

## Performance notes

- Source validation now uses `asyncio` + `aiohttp` instead of spinning thousands of threads, cutting CPU/RAM overhead while keeping high concurrency.
- Proxy list writes are deduped in-memory before flushing to disk.
- Optional Cython accelerators live in `utils.pyx` (unique-preserve + fast line counting). Build with `python setup.py build_ext --inplace` if you want the native speedup.

## Planned Features

- Implement SOCKS4 & SOCKS5 validation.
- Add CLI tuning flags for concurrency/timeout.
- Discerning between Elite, Anonymous, and Transparent anonymity classes of proxies.

## Support

Need help and can't get it to run correctly? Open an issue or use the [contact page](https://solanaceae.xyz/).

## Sponsorship

If you like what I do, buy me boba so I can continue developing this tool and others!
[Ko-Fi](https://ko-fi.com/solanaceae)

## Changelog

[Release v2.6](https://github.com/0xSolanaceae/proXXy/releases/tag/v2.6)

- [Full changelog](https://github.com/0xSolanaceae/proXXy/compare/v2.5...v2.6)

---

## License

This project is licensed under the GNU General Public License v3.0 License. See the `LICENSE` file for more information.
