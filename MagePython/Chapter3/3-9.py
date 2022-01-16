#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Jim Huang
@contact:Jim_Huang@trendmicr.com
@version: 1.0.0
@license: Apache Licence
@file: 3-9.py
@time: 2020/12/1 16:31
"""
import random
import  string
words = []
counter = {}
alpha = string.ascii_lowercase
for _ in range(100):
    words.append(random.choice(alpha) + random.choice(alpha))
for i in words:
    counter[i] = counter.get(i,0) + 1
print(counter)
print(sorted(counter.items(),reverse=True))