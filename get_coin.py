import requests
import json

symbols = ["BTCUSDT", "ETHUSDT", "SUIUSDT", "BNBUSDT", "XRPUSDT",
           "ADAUSDT", "SOLUSDT", "DOGEUSDT", "DOTUSDT", "AVAXUSDT"]

url = "https://api.binance.com/api/v3/ticker/price"
params = {"symbols": json.dumps(symbols, separators=(',', ':'))}   # Binance wants a JSON array string

data = requests.get(url, params=params).json()
print("TYPE:", type(data))     # <-- add this
print("DATA:", data)  
for item in data:
    print(f"{item['symbol']}: {float(item['price'])}")