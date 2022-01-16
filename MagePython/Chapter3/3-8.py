#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Jim Huang
@contact:Jim_Huang@trendmicr.com
@version: 1.0.0
@license: Apache Licence
@file: 3-8.py
@time: 2020/12/1 15:34
"""
import random
import collections
lst = []
dict1 = {}
od = collections.OrderedDict()
for _ in range(100):
    lst.append(random.randint(-1000,1000))
for i in lst:
    dict1[i] = dict1.get(i,0) + 1
keyorder = sorted(list(dict1.keys()))

for i in keyorder:
    od[i] = dict1[i]
print(od)
print(sorted(dict1.items()))
