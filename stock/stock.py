# coding=utf-8
import sys
import os
import tushare as ts
os.system('del 000425.csv')
df = ts.get_k_data('000425', '2017-01-01', '2018-04-19')

del df['code']

df.to_csv('f:/vpython/000426.csv')
