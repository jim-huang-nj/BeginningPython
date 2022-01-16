'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2020-11-29 11:29:17
LastEditors: CoderXZ
LastEditTime: 2021-05-01 10:18:50
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Jim Huang
@contact:Jim_Huang@trendmicr.com
@version: 1.0.0
@license: Apache Licence
@file: 2-3.py
@time: 2020/11/20 11:01
# 3 个数排序
"""
a = int(input("Please enter the first number:"))
b = int(input("Please enter the second number:"))
c = int(input("Please enter the third number:"))
lst = [a,b,c]
if a > b:
    big = a
    small = b
else:
    big = b
    small = a
if c < small:
    medium = small
    small = c
if  (c > small and c < big):
    medium = c
if c > big:
    medium = big
    big = c
print("Max:{0},Med:{1},Min:{2}".format(big,medium,small))
print("Max is {}".format(max(lst)))
lst.sort(reverse=True)
print(lst)



