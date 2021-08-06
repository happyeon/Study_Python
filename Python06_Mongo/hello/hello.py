# -*- coding:utf-8 -*-

# pip install pymongo
from pymongo import MongoClient

# 둘 중에 편한 걸로 사용하면 됨
client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')

# 둘 중에 편한 걸로 사용하면 됨
db = client.test
# db = client['test']

# 둘 중에 편한 걸로 사용하면 됨
collection = db.score
# collection = db['score']

result = collection.find()
# print(result)             # cursor: 일회용 객체

for res in result:
    print(res)