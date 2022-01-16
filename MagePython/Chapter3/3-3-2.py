'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-03 06:03:47
LastEditors: CoderXZ
LastEditTime: 2021-05-03 06:06:58
'''
from collections import OrderedDict
import random
d = {'banana':3 ,'apple':4,'pear':1,'orange':2}
print(d)

keys = list(d.keys())
random.shuffle(keys)
print(keys)
od = OrderedDict()
for key in keys:
    od[key] = d[key]
print(od)
print(od.keys())