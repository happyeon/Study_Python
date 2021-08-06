# -*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test 
collection = db.score 


# res01 = collection.insert_one({'name': '김서형', 'kor': 99, 'eng': 100, 'math':99})
# print(res01.inserted_id)

for doc in collection.find():
    print(doc)

'''
res02 = collection.insert_many(
    [
        {'name':'이보영', 'kor': 100, 'eng': 99, 'math': 89},
        {'name':'김헤수', 'kor': 90, 'eng': 79, 'math': 80},
        {'name':'박보영', 'kor': 80, 'eng': 100, 'math': 99}
    ]
)

print(res02.inserted_ids)
'''

for doc in collection.find():
    print(doc)