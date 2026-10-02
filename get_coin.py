import requests
import json


# import requests
# import json

# symbols = ["BTCUSDT", "ETHUSDT", ...]

# url = "https://api.binance.com/api/v3/ticker/price"
# params = {"symbols": json.dumps(symbols, separators=(",", ":"))}
# data = requests.get(url, params=params).json()

# for item in data:
#     print(f"{item['symbol']}: {float(item['price']):,.4f}")


symbols = ["BTCUSDT", "DOGEUSDT", "SUIUSDT", "XRPUSDT", "LTCUSDT",
           "HYPEUSDT", "SOLUSDT", "ZECUSDT", "DOTUSDT", "AAVEUSDT"]

url = "https://api.binance.com/api/v3/ticker/price"
params = {"symbols": json.dumps(symbols, separators=(',', ':'))}   # Binance wants a JSON array string

data = requests.get(url, params=params).json()
print("TYPE:", type(data))     # <-- add this
print("DATA:", data)  
for item in data:
    print(f"{item['symbol']}: {float(item['price'])}")