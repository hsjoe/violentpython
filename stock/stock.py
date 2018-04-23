# coding=utf-8

import tushare as ts

df = ts.get_k_data('000425', '2017-01-01', '2018-04-19')
# df.to_csv('c:/Users/IBM/Desktop/000425.csv')
df.