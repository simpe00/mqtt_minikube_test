# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:36:34 2021

@author: Simsi
"""
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

""""
actionsDel = [
  {
    "delete":{
    "_index": "countryvaccinations",
    "_id": "CV"+str(j)
    }
  }
  for j in range(0, 3000)
]
"""


def search():
    query_all = {
        "size": 3,
        "query": {
            "match": {
                "_id": "CV*"
            }
        }
    }

    resp = es.search(index="countryvaccinations", body=query_all)

    tempStruc = resp['hits']['hits']
    print(tempStruc)


def delete():
    for j in range(0, 3081):
        es.delete(index="countryvaccinations", id="CV"+str(j))


if __name__ == '__main__':
    # search()
    delete()
