# -*- coding:utf-8 -*-

# with : close 자동으로 해줌
with open('test01.txt', 'r') as file:
    a = file.read()
    print(a)