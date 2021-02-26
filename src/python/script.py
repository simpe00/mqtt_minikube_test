from elasticsearch import Elasticsearch
import time # for the index's ""timestamp"" field
from datetime import datetime


# connect to the Elasticsearch cluster
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# or: Elasticsearch([{'host': 'localhost', 'port': 9200}])

'''
The 'hosts' parameter is optional:
elastic = Elasticsearch(hosts=[""DOMAIN_NAME""])

Optional dictionary parameter to pass:
{'host': ""SOME_DOMAIN"", 'port': 1234, 'url_prefix': 'en', 'use_ssl': True}
'''
# Kibana console request:
# GET some_index/_mapping

# cURL request:
# curl -XGET localhost:9200/some_index/_mapping/?pretty

doc1 = {
    'date': '2021-01-09',
    'people_vaccinated': 447.0,
    'country': 'Albania',
    'daily_vaccinations_raw': 142.0,
    'people_vaccinated_per_hundred': 0.02,
    'vaccines': 'Pfizer/BioNTech',
    'daily_vaccinations_per_million': 19.0,
    'daily_vaccinations': 250.0,
    'total_vaccinations': 447.0,
    '@timestamp': '2021-01-09T00:00:00.000+01:00',  # <- X-Axis
    'total_vaccinations_per_hundred': 0.22,
    'iso_code': 'ALB',
    'source_name': 'pythonScript',
    'source_website': 'www.dummy.com'
}

timestamp = int(time.time())
print("EPOCH:", timestamp)

# es.indices.create(index="countryvaccinations1",body=doc1)

"""
es.indices.create(index='some-new-index')

res = es.get(index="countryvaccinations", id="XpdQpXcBoIxz4vaQrI31")

print(res['_source'])

# chanching something
res['_source']['daily_vaccinations'] = 250.0

es.index(index="countryvaccinations",
         id="XpdQpXcBoIxz4vaQrI31", body=res['_source'])

es.delete(index='countryvaccinations', id=1)
es.index(index="countryvaccinations", id=2, body=doc1)
res = elastic.get(index="countryvaccinations", id=2)
"""