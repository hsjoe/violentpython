# coding=utf-8
import pandas as pd
import numpy as np
import sys
import os
import tushare as ts
import matplotlib.pyplot as plt

stock_code = input('Please input your stock code ')

file_name = 'F:/violentpython/%s'%stock_code
del_file_name = 'del %s'%file_name
os.system(del_file_name)


#601231
df = ts.get_k_data('601231') 
df = df.drop('code', axis=1)

df['sema'] = pd.Series(df['close']).ewm(span=12).mean()
df['lema'] = pd.Series(df['close']).ewm(span=26).mean()

df['dif'] = df['sema'] - df['lema']
df['dea'] = pd.Series(df['dif']).ewm(span=12).mean()
#df = df.round({'dif':2,'dea':2})

df['macd'] = 2*(df['dif']-df['dea'])

#df = df.round({'dif':2,'dea':2})


df.to_csv(file_name)

