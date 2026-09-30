# Cryptocurrency Builder

This project is a simple Python script collection for fetching live cryptocurrency prices from the Binance public API.

## Overview

The project currently contains two example scripts:

- `get_price.py` — fetches the current price of `BTCUSDT`
- `get_coin.py` — fetches prices for multiple coins at once

## Features

- Fetch live market prices from Binance
- Easy to run from a local Python environment
- Beginner-friendly example for working with crypto APIs

## Requirements

- Python 3.x
- `requests` package

Install dependencies with:

```bash
pip install requests
```

If you are using the project virtual environment in this workspace, you can run:

```bash
env\Scripts\python -m pip install requests
```

## Run the scripts

### 1. Single coin price

```bash
env\Scripts\python get_price.py
```

Example output:

```text
Current price of BTCUSDT: 62483.12
```

### 2. Multiple coin prices

```bash
env\Scripts\python get_coin.py
```

This script requests prices for several symbols including:

- BTCUSDT
- ETHUSDT
- SUIUSDT
- BNBUSDT
- XRPUSDT
- ADAUSDT
- SOLUSDT
- DOGEUSDT
- DOTUSDT
- AVAXUSDT

## Notes

- This project uses Binance's public ticker API.
- Prices may change quickly because they are live market values.
- API access depends on internet connectivity and Binance service availability.

## Project Files

- `get_price.py` — simple BTC price example
- `get_coin.py` — multi-coin price example
- `readme.txt` — initial notes from the early learning stage
- `readme.md` — project documentation

## License

This project is for learning and experimentation purposes.
