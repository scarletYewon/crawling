#패키기 가져오기
import urllib.request

import bs4
import openpyxl
import requests
from bs4 import BeautifulSoup

url = "https://map.naver.com/v5/search/%EC%9D%B4%EC%83%81%EA%B0%88%EB%B9%84/place/11852057?c=14139502.0818882,4523621.2948617,15,0,0,0,dh&placePath=%3Fentry%253Dbmp"
html = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(html, 'html.parser')
# li = soup.find("li",{"class":"_3FaRE"})
# sp = li.findAll("span",{"class":"WoYOw"})
print(soup)


