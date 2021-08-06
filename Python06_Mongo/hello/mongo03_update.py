# -*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
test = client['test']
score = test['score']

# document 하나만 찾아서 수정하는 함수를 사용하여!
# 조세호의 수학 점수를 10점으로 변경하자
# https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html
res01 = score.update_one(
    {'name': '조세호'},
    {'$set': {'mat': 10}}
)

print(res01.matched_count)
print(res01.modified_count)

print('--------------------')

res02 = score.update_many(
    {'eng': {'$lte': 70}},
    {'$set':{'eng':0}}
)

print(res02.matched_count)
print(res02.modified_count)