#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Jim Huang
@contact:Jim_Huang@trendmicr.com
@version: 1.0.0
@license: Apache License
@file: 2-2.py
@time: 2020/11/20 9:39
# 杨辉三角形
"""
n = 11
lst=[[1],[1,1]]
for x in range(2,n):
    cur = []
    for y in range(0,x+1):
        if y==0 or y==x:
            cur.append(1)
        else:
            cur.append(lst[x-1][y-1]+lst[x-1][y])
    lst.append(cur)

for x in range(n):
    print("    "*(11-x),end="")
    for y in range(len(lst[x])):
        print("{0:4}".format(lst[x][y])+" "*4,end="")
    print()


lst = []
for i in range(1,n):
    lst1 = []
    for j in range(1,i+1):
        if j == 1 or j == i:
            lst1.append(1)
        else:
            item = lst[i-2][j-2] + lst[i-2][j-1]
            lst1.append(item)
    lst.append(lst1)
print(lst)

for x in range(len(lst)):
    print("   "*(11-x),end="")
    for y in range(len(lst[x])):
        print("{0:^3}".format(lst[x][y])+" "*3,end="")
    print()
            