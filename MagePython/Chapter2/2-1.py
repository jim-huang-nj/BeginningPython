'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2020-11-29 11:29:17
LastEditors: CoderXZ
LastEditTime: 2021-05-01 09:26:36
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Jim Huang
@contact:Jim_Huang@trendmicr.com
@version: 1.0.0
@license: Apache Licence
@file: 2-1.py
@time: 2020/11/19 17:54
"""
# 质数的优化算法
import  datetime
start = datetime.datetime.now()
count = 0
primenumber = []
for x in range(2,100000):
    for i in primenumber:
        if x % i == 0:
            break
    else:
        primenumber.append(x)
        count +=1
time = (datetime.datetime.now()-start).total_seconds()
print(count)
#print(primenumber)
print(time)
print("-"*30)


start = datetime.datetime.now()
count = 1
primenumber = [2]
flag = False
for x in range(3,100000,2):
    for i in primenumber:
        if x % i == 0:
            flag = True
            break
        if i > (x/2):
            flag = False
            break

    if not flag:
        primenumber.append(x)
        count +=1
time = (datetime.datetime.now()-start).total_seconds()
print(count)
#print(primenumber)
print(time)
print("-"*30)

start = datetime.datetime.now()
count = 1
primenumber = [2]
flag = False
for x in range(3,100000,2):
    for i in primenumber:
        if x % i == 0:
            flag = True
            break
        if i > (x**0.5):
            flag = False
            break

    if not flag:
        primenumber.append(x)
        count +=1
time = (datetime.datetime.now()-start).total_seconds()
print(count)
#print(primenumber)
print(time)
print("-"*30)