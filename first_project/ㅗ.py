import requests

from bs4 import BeautifulSoup
nurl = "https://www.naver.com"

r = requests.get(nurl):
print(r.status_code)
print(r.text)

bs = BeautifulSoup(r.text, 'html.parser')

ranks = bs.select('a.ah_a')

for tag in ranks :
    print(rtag.text)