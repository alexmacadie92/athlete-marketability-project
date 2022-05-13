#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:09:43 2022

@author: alexandermacadie
"""

import pandas as pd                        
from pytrends.request import TrendReq
from time import sleep
from random import randint


pytrends = TrendReq(timeout=(10,25))

### RUN YOUR LIST OF ATHLETES TO COLLECT THEIR GTREND CODE

keywords = ['LeBron James', 'Kobe Bryant', 'Lionel Messi']  ###PUT YOUR LIST OF ATHLETES HERE


df_codes = pd.DataFrame(columns=['Keyword','Code','Title','Type'])


for word in keywords:
    sleep(randint(2,3))
    df_suggest = pd.DataFrame.from_dict(pytrends.suggestions(keyword=word))
    try:
        code = df_suggest['mid'][0]
    except:
        code = None
    try:
        title = df_suggest['title'][0]
    except:
        title = None
    try:
        typ = df_suggest['type'][0]
    except:
        typ = None
        
    to_append = [word,code,title,typ]
    df_codes.loc[len(df_codes)]=to_append

print(df_codes)


### RUN TO FIX UP ANY INCORRECT CODES

pd.DataFrame.from_dict(pytrends.suggestions(keyword="Kobe Bryant"))