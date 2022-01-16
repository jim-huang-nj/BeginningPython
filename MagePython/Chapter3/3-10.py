#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Jim Huang
@contact:Jim_Huang@trendmicr.com
@version: 1.0.0
@license: Apache Licence
@file: 3-10.py
@time: 2020/12/2 10:15
# 列表解析式
"""
import  random
lst = [pow(i,2) for i in range(1,11)]
print(lst)


lst1 = [1,4,9,16,25,10,15]
lst2 = [ lst1[j]+lst1[j+1] for j in range(len(lst1)-1) ]
print(lst2)

[print("{}*{}={:<3}".format(j,i,j*i),end="\n" if i==j else "") for i in range(1,10)  for j in range(1,i+1)]


