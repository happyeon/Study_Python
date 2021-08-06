# -*- coding:utf-8 -*-

# pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup

tag = input('search tag :  ')
url = 'https://www.instagram.com/explore/tags/' + tag

driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')    # 브라우저를 우리 대신 켜줌

driver.implicitly_wait(10)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_list = soup.find_all('div', class_='KL4Bh')
#print(img_list[0])
for imgs in img_list:
    print(imgs.img['src'])

driver.close()
driver.quit()