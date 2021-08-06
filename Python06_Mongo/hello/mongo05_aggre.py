# -*- coding:utf-8 -*-

from pymongo import MongoClient
from pprint import pprint


client = MongoClient('mongodb://localhost:27017')
test = client.test
score = test.score


# math 점수가 90보다 큰 document들의
# math 평균을 구해서, {'_id':'math', 'average': 평균}을 출력
aggre = score.aggregate(
    [
        {'$match': {'math': {'$gt': 90}}},
        {'$group': {'_id': 'math', 'average': {'$avg': '$math'}}}
    ]
)
print(aggre)            # CommandCursor = ?
pprint(list(aggre))