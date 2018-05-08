# coding=utf-8
import pandas as pd
import numpy as np

import time
import sys
import os

import tushare as ts
import matplotlib.pyplot as plt

stock_code = input('Please input your stock code: ')
folder = time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())
os.makedirs(r'%s/%s'%(os.getcwd(),folder))
file_name = r'%s/%s/%s.csv'%(os.getcwd(),folder,stock_code)


df = ts.get_k_data(stock_code, start='2016-01-01', end='2018-05-04') 
df = df.drop('code', axis=1)
df = df.drop('volume', axis=1)

df['sema'] = pd.Series(df['close']).ewm(span=12).mean()
df['lema'] = pd.Series(df['close']).ewm(span=26).mean()

df['dif'] = df['sema'] - df['lema']
df['dea'] = pd.Series(df['dif']).ewm(span=9).mean()
df = df.round({'dif':2,'dea':2})

df['macd'] = 2*(df['dif']-df['dea'])
df['flag'] = None
ds = df.index[df['macd'] == 0].tolist()

for i in ds:
    if df.iloc[i+1, 7] > df.iloc[i+1, 8]:
        df.iloc[i+1, 10] = '上升'
    elif df.iloc[i+1, 7] < df.iloc[i+1, 8]:
        df.iloc[i+1, 10] = '下降'
    else:
        continue

df.to_csv(file_name)






