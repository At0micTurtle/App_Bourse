import requests
import json

# API URL
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=SHOP.TRT&outputsize=full&apikey=demo"
response = requests.get(url)
data = response.json()

print(data)