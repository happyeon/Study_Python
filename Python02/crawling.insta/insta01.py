# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

tag = input('search tag :  ')
url = 'https://www.instagram.com/explore/tags/' + tag

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

print(soup.find('div', {'class', 'KH4Bh'}))     # 옛날 방식
