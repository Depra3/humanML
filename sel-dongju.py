# page 31 ~
from bs4 import BeautifulSoup
import urllib.request as req

# #mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

a_list = soup.select('#mw-content-text > div > ul > li a')

for a in a_list:
    name = a.string
    print("-", name)