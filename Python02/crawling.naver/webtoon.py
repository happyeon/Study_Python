# -*- coding:utf-8 -*-

# pip install requests
from bs4 import BeautifulSoup
import requests
import json

url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=thu'

resp = requests.get(url)
# print(resp.text)
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)

img_list = soup.find('ul', class_='img_list')

webtoons = img_list.select('dl')

lst = list()
for webtoon in webtoons:
    title = webtoon.find('a')['title']      # text로 해도 되는데 text는 특정 길이 이상은 뒷 부분이 ...으로 출력된다.
    star = webtoon.find('strong').text
    # print('{} [{}]'.format(title, star))
    tmp = {}
    tmp['title'] = title
    tmp['star'] = star
    lst.append(tmp)

#print(lst)
res = {}
res['webtoons'] = lst

res_json = json.dumps(res, ensure_ascii=False)
# print(res_json)

with open('webtoons.json', 'w', encoding='utf-8') as f:
    f.write(res_json)
