'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2020-12-06 09:32:17
LastEditors: CoderXZ
LastEditTime: 2021-05-01 16:14:31
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Jim Huang
@contact:Jim_Huang@trendmicr.com
@version: 1.0.0
@license: Apache Licence
@file: 2-5.py
@time: 2020/11/24 13:54
# 置换矩阵
"""
lst = [[1,2,3],[4,5,6],[7,8,9]]
#lst =[[1,2,3],[4,5,6]]
newlst = list()
for i in range(len(lst[0])):
    tmplst=list()
    for j in range(len(lst)):
        #a = lst[i][j]
        tmplst.append(lst[j][i])
        #print(a)
    newlst.append(tmplst)
for i in range(len(newlst)):
    print(newlst[i])
