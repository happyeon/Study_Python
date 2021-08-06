# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)

inner_value = soup.find_all(class_='inner_value')
# inner_value = soup.select('dd ul li p')

#print(inner_value)

result = '''국내발생: {}
해외유입: {}
소    계: {}
'''.format(inner_value[1].text, inner_value[2].text, inner_value[0].text.split(' ')[1]) 
print(result)