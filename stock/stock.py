# coding=utf-8
import sys
import os
import tushare as ts
os.system('del 000425.csv')
df = ts.get_k_data('000425', '2017-01-01', '2018-04-19')
<<<<<<< HEAD
# df.to_csv('c:/Users/IBM/Desktop/000425.csv')
df.
=======

del df['code']

df.to_csv('f:/vpython/000426.csv')
>>>>>>> 11aeb100af218d205e863e2627e0f9495733fad5
