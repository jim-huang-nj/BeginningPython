#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Jim Huang
@contact:Jim_Huang@trendmicr.com
@version: 1.0.0
@license: Apache Licence
@file: 3-7.py
@time: 2020/12/1 15:22
"""
lst = input("Please enter number:")
counter = {}
for c in lst:
    # if c not in counter.keys():
    #     counter[c] = 0
    # counter[c] +=1
    counter[c] = counter.get(c,0) + 1

print(counter)