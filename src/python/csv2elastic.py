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
#from elasticsearch import helpers
# from datetime import datetime

# https://towardsdatascience.com/exporting-pandas-data-to-elasticsearch-724aa4dd8f62
# https://stackoverflow.com/questions/49726229/how-to-export-pandas-data-to-elasticsearch/49982341

es = Elasticsearch([{'host': '172.20.0.3', 'port': 9200}])
        
def rec_to_actions(df,indexStr):
    import json
    for record in df.to_dict(orient="records"):
        yield ('{ "index" : { "_index" : "%s"}}'% (indexStr))
        yield (json.dumps(record, default=int))

def df2el(DataFrame, indexStr):

    # add timestamp
    DataFrame['@timestamp']=DataFrame['date']+'T00:00:00.000+01:00'    

    # send to es    
    es.bulk(rec_to_actions(DataFrame,indexStr))


if __name__ == "__main__":

    timeStart = time.time()

    # open csv
    path = dir_path = os.path.dirname(os.path.realpath(__file__))+'/../res/'
    filename = 'country_vaccinations.csv'

    df = pd.read_csv(path+filename, na_filter=True).fillna(value=0)

    df2el(df, "countryvaccinations")

    timeStop = time.time()

    # calc time
    timeCalc = timeStop-timeStart
    print("calculation: "+str(timeCalc)+" sec.")

    es.indices.flush(index="countryvaccinations")
