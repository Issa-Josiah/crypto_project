# import requests
# import json

# symbols = ["BTCUSDT", "DOGEUSDT", "SUIUSDT", "XRPUSDT", "LTCUSDT",
#            "HYPEUSDT", "SOLUSDT", "ZECUSDT", "DOTUSDT", "AAVEUSDT"]

# def get_coin_prices(symbols):
#     url = "https://api.binance.com/api/v3/ticker/price"
#     params = {"symbols": json.dumps(symbols, separators=(',', ':'))}
#     data = requests.get(url, params=params).json()

#     prices = {}
#     for item in data:
#         prices[item['symbol']] = float(item['price'])
#     return prices

# results = get_coin_prices(symbols)
# print(results)

    
    




















import requests
import json

symbols = ["BTCUSDT", "DOGEUSDT", "SUIUSDT", "XRPUSDT", "ZECUSDT"]

def hooray (symbols):
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {"symbols": json.dumps(symbols, separators=(',', ':'))}
    data = requests.get(url, params=params).json()

    prices = {}
    for item in data:
        prices[item['symbol']] = float(item['price'])
    return prices

results = hooray(symbols)
print(results)
