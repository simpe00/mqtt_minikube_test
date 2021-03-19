# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:22:48 2021

@author: Simsi
"""

# open csv

import pandas as pd
import os
import numpy as np
from elasticsearch import Elasticsearch
import time
import logging
# from elasticsearch import helpers
# from datetime import datetime

# https://towardsdatascience.com/exporting-pandas-data-to-elasticsearch-724aa4dd8f62
# https://stackoverflow.com/questions/49726229/how-to-export-pandas-data-to-elasticsearch/49982341

es = Elasticsearch([{
    'host': os.getenv('IPV4_ADRR'),
    'port': int(os.getenv('PORT_ELASTIC_1'))
    }])


# https://stackoverflow.com/questions/49726229/how-to-export-pandas-data-to-elasticsearch/49982341
def df2bulkjson(df, indexStr):
    import json
    import uuid
    for record in df.to_dict(orient="records"):
        yield ('{ "index" : { "_index" : "%s", "_id" : "%s"}}'
               % (indexStr, 'CV'+record['date']+str(uuid.uuid4())))
        yield (json.dumps(record, default=int))


def main(indexname, filename):
    # start calculation time
    timeStart = time.time()

    # open csv
    path = os.path.dirname(os.path.realpath(__file__))+'/../res/'
    df = pd.read_csv(path+filename, na_filter=True).fillna(value=0)

    # add timestamp
    df['@timestamp'] = df['date']+'T00:00:00.000+01:00'

    # send to es
    es.bulk(df2bulkjson(df, indexname))

    # calc time
    timeCalc = time.time()-timeStart
    logging.info("calculation Time: "+str(timeCalc)+" sec.")


def TEST():
    return 10


if __name__ == "__main__":
    main("countryvaccinations", 'country_vaccinations.csv')
