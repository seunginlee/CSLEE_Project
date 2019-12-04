import requests

surch = "https://api.darksky.net/forecast/3456d9e5943bd3e59a9b28fd907604c8/37.8267,-122.4233 "

response = requests.get(surch)
print(response.status_code)
if response.status_code == 200:
    weather = json.loads(response.text)
    print(type(weather))
    print("위도",weather["latitude"])

