# coding=utf-8
import pandas as pd
import numpy as np
import sys
import os
import tushare as ts
import matplotlib.pyplot as plt

os.system('del E:/violent_python/000425.csv')

df = ts.get_k_data('000425') 
df = df.drop('code', axis=1)
df['sema'] = pd.Series(df['close']).ewm(span=12).mean()
df['lema'] = pd.Series(df['close']).ewm(span=26).mean()

df['dif'] = df['sema'] - df['lema']
df['dea'] = pd.Series(df['dif']).ewm(span=12).mean()

df['macd'] = 2*(df['dif']-df['dea'])

df = df.round({'dif':2,'dea':2,'macd':2})

filename = r'E:/violent_python/000425.csv'
df.to_csv(filename)

