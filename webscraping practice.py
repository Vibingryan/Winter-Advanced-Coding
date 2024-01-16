import requests
from bs4 import BeautifulSoup

url = "https://www.pomfret.org/athletics/schedule"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print(soup.find("td", "fsTitle"))
