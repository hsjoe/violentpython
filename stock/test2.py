<<<<<<< HEAD

# coding=utf-8
import pandas as pd
import numpy as np

import time
import sys
import os
import shutil

import tushare as ts
import matplotlib.pyplot as plt

stock_code = input('Please input your stock code: ')
folder = time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())
os.makedirs(r'%s/%s'%(os.getcwd(),folder))
file_name = r'%s/%s/%s.csv'%(os.getcwd(),folder,stock_code)

df = ts.get_k_data(stock_code, start='2016-01-01', end='2018-05-04')

df.to_csv(file_name)
=======
import array

a = array.array('i',[1,2,3])

print(type(a))
>>>>>>> feccbe913d028f8d6ad8bcea3e07be387298687a
