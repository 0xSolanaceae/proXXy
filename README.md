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
python proXXy.py --concurrency 200 --timeout 8
```

The program will modify four files in the `output/` directory with your proxies:

- `HTTP.txt`
- `HTTPS.txt`
- `SOCKS4.txt`
- `SOCKS5.txt`

 with a logfile (`error.log`) with warnings/errors.

### Speeding up validation

Validation now has tunable knobs and early exit:

```bash
python proXXy.py -V \
  --val-concurrency 800 \
  --val-timeout 2 \
  --val-limit 50000
```

- `--val-concurrency`: how many proxies to test in parallel (higher is faster until your network or the judge sites throttle).
- `--val-timeout`: per-proxy timeout seconds.
- `--val-limit`: stop once this many valid proxies are found (0 = validate everything).

## Flags

Syntax for running proXXy is as follows:

```bash
usage: proXXy.py [-h] [--validate] [--update] [--version] [--src_check]
                 [--concurrency CONCURRENCY] [--timeout TIMEOUT]
                 [--val-concurrency VAL_CONCURRENCY] [--val-timeout VAL_TIMEOUT]
                 [--val-limit VAL_LIMIT]
```

1. `-V, --validate`: Validate HTTP/HTTPS outputs after scraping.
2. `-u, --update`: Run the update script and exit.
3. `-h, --help`: Show help.
4. `-v, --version`: Print the script version and exit.
5. `-s, --src_check`: Check sources and show counts only.
6. `--concurrency / --timeout`: Tuning for source fetching.
7. `--val-concurrency / --val-timeout / --val-limit`: Tuning for validation speed and early exit.

```bash
usage: proXXy.py [-h] [--validate] [--update] [--version] [--src_check]
                 [--concurrency CONCURRENCY] [--timeout TIMEOUT]
                 [--val-concurrency VAL_CONCURRENCY] [--val-timeout VAL_TIMEOUT]
                 [--val-limit VAL_LIMIT]

Fast async proxy scraper; scraping & checking HTTP, HTTPS, SOCKS4, & SOCKS5 proxies.

options:
  -h, --help            show this help message and exit
  --validate, -V        Validate proxies after scraping (default: False)
  --update, -u          Run the update script and then exit
  --version, -v         Print the version of the script and exit
  --src_check, -s       Verify sources only and exit
  --concurrency, -c     Concurrent source fetches (default: 120)
  --timeout, -t         Per-source timeout seconds (default: 8)
  --val-concurrency     Validation concurrency (default: 400)
  --val-timeout         Validation timeout seconds (default: 3)
  --val-limit           Stop validation after N valid proxies (0 = no limit)
```

## Performance notes

- Source scraping and validation both use `asyncio` + `aiohttp` with configurable concurrency/timeouts.
- Validation can stop early via `--val-limit` to avoid hours-long runs when you only need N good proxies.
- Proxy list writes are deduped in-memory before flushing to disk.

## Planned Features

- Implement SOCKS4 & SOCKS5 validation.
- Discerning between Elite, Anonymous, and Transparent anonymity classes of proxies.

## Support

Need help and can't get it to run correctly? Open an issue or use my [contact page](https://solanaceae.xyz/).

## Sponsorship

If you like what I do, buy me boba so I can continue developing this tool and others!
[Ko-Fi](https://ko-fi.com/solanaceae)


---

## License

This project is licensed under the GNU General Public License v3.0 License. See the `LICENSE` file for more information.
