#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Jim Huang
@contact:Jim_Huang@trendmicr.com
@version: 1.0.0
@license: Apache Licence
@file: 1-12.py
@time: 2020/11/19 8:01
"""
# 10w 内质数的时间效率
import datetime
upper_limit = 100000
count=0
start = datetime.datetime.now()
for x in range(2,upper_limit):
    for i in  range(2,int(x/2)+1):
        if x % i ==0:
            break
    else:
        count+=1
deltatime = (datetime.datetime.now()-start ).total_seconds()
print("The number is "+str(count))
print("The way 1 time is "+ str( deltatime))

start = datetime.datetime.now()
count = 1
for x in range(3,upper_limit,2):
    for i in  range(3,int(x/2)+1,2):
        if x % i ==0:
            break
    else:
        #print(x)
        count+=1
deltatime = (datetime.datetime.now()-start ).total_seconds()
print("The number is "+str(count))
print("The way 2 time is "+ str( deltatime))
