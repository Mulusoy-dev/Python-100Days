import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=TRY&from=USD&amount=1"

payload = {}
headers= {
  "apikey": "z3KjDNKBu88ddQwgUKjU5M6Lg3djpPEm"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(result)
