import requests
import json

base_key = "USD"
sym_key = "RUB"
amount = 100

r = requests.get(f"https://api.exchangeratesapi.io/v1/latest/9dc87b58024bab46297da516eadfcdd2/pair/USD/RUBbase={base_key}&symbols={sym_key}")
print(r.content)