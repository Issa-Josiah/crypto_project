import requests

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
response = requests.get(url)
data = response.json()
price = float(data["price"])
print(f"Current price of BTCUSDT: {price}")
