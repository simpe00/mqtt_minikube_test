# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:36:34 2021

@author: Simsi
"""
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch([{'host': '172.20.0.3', 'port': 9200}])

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
query_all_0 = {
    "size": 3,
    "query": {
        "match": {
            "iso_code": "ALB"
        }
    }
}

query_all_1 = {
    "size": 3,
    "query": {
        "bool": {
            "must": [
                { "match": { "iso_code":"ALB" }},
                { "match": { "date": "2021-01-20" }}
            ]
        }
    }
}

def search():
    resp = es.search(index="countryvaccinations", body=query_all_1)
    tempStruc = resp['hits']['hits']

    return tempStruc[0]['_id']


def delete(id):
    es.delete(index="countryvaccinations", id=id)


if __name__ == '__main__':
    a = search()
    delete(a)
