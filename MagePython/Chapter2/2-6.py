#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Jim Huang
@contact:Jim_Huang@trendmicr.com
@version: 1.0.0
@license: Apache Licence
@file: 2-6.py
@time: 2020/11/24 14:11
# 随机数
"""
import  random
lst = list()
repeatlst = list()
for _ in range(10):
    randomnub = random.randint(1,20)
    lst.append(randomnub)
print(lst)
num = 1
i = 0
while (i < (len(lst))):
    num = lst.count(lst[i])
    if (num > 1) :
        repeatlst.append(lst[i])
        for _ in range(num):
            lst.remove(lst[i])
        num = 0
    i = i+1
print("repeated numbers has "+ str(len(repeatlst))+",",end="")
print(repeatlst)
print("different number has "+ str(len(lst))+":",end="")
print(lst)