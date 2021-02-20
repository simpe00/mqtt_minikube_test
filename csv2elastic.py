# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:22:48 2021

@author: Simsi
"""

# open csv

import pandas as pd
import os
from elasticsearch import Elasticsearch
from elasticsearch import helpers
# from math import isnan
import time
# from datetime import datetime

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def docCSV2el(docCSV, indexStr):

    bulkList = []
    temp1 = {}

    # read each row -> Doc in elastic
    for row in docCSV.index:

        # allocate dic
        tempDoc = {}
        for col in docCSV:
            tempDoc[col] = docCSV.iloc[row][col]
        # add timestamp
        tempDoc['@timestamp'] = tempDoc['date']+'T00:00:00.000+01:00'

        # add header
        temp1 = {
            "_index": indexStr,
            "_type": "_doc",
            "_id": "CV"+str(row),
            "_source": tempDoc
        }

        bulkList.append(temp1)

    # send to es
    helpers.bulk(es, bulkList)


if __name__ == "__main__":

    timeStart = time.time()

    # open csv
    path = os.getcwd()+'/'
    filename = 'country_vaccinations.csv'
    docCSVCovVac = pd.read_csv(path+filename, na_filter=False)

    docCSV2el(docCSVCovVac, "countryvaccinations")

    timeStop = time.time()

    # calc time
    timeCalc = timeStop-timeStart
    print("calculation: "+str(timeCalc)+" sec.")

    es.indices.flush(index="countryvaccinations")
