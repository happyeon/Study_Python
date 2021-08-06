# -*- coding:utf-8 -*-

# https://pymongo.readthedocs.io/en/stable/tutorial.html

from pymongo import MongoClient
import pprint


# client
client = MongoClient('localhost', 27017)
# db
test = client.test
# collection
score = test.score

cursor = score.find()

for doc in cursor:
    # print(doc)
    pprint.pprint(doc)

print('--------------')

# shin = score.find({'name':'신동엽'})
shin = score.find_one({'name':'신동엽'})
pprint.pprint(shin)

print('--------------')

# 국어 점수가 60보다 큰 도규먼트들을 모두 출력하자.
kors = score.find({'kor': {'$gt': 60}})
for doc in kors:
    pprint.pprint(doc)

print('--------------')

print('score collection 안에 있는 document의 총 갯수 : ', score.count_documents({}))