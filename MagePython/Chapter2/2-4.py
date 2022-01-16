#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Jim Huang
@contact:Jim_Huang@trendmicr.com
@version: 1.0.0
@license: Apache Licence
@file: 2-4.py
@time: 2020/11/20 13:46
# 冒泡法
"""
num_list = list(range(100,0,-1))
print(num_list)
for i in range(len(num_list)-1):
    for j in range(0,len(num_list)-1):
        if num_list[j] > num_list[j+1]:
            swap = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] =swap
print(num_list)
