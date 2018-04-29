# coding=utf-8
import pandas as pd
import numpy as np

import sys
import os
import tushare as ts
import matplotlib.pyplot as plt
os.system('del 000425.csv')
df = ts.get_k_data('000425', '2017-01-01', '2018-04-19')
df.set_index('date')
#print(type(df))
del df['code']
del df['volume']
del df['high']
del df['low']
filename = 'E:/violent_python/000425.csv'


#df.plot()
df.to_csv(filename)


df.plot(x='date')
plt.figure() 
plt.show()