'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2020-12-06 09:32:17
LastEditors: CoderXZ
LastEditTime: 2021-05-01 21:39:37
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Jim Huang
@contact:Jim_Huang@trendmicr.com
@version: 1.0.0
@license: Apache Licence
@file: 3-1.py
@time: 2020/11/25 13:35
"""
lst =[1,(2,3,4),5]
a,(b,c,d),e = lst
print(a,b,c,d,e)

_,(*_,val),*_ = lst
print(val)
print(_)

_,[*_,val],*_ = lst
print(val)

key,_,val = "JAVA_HOME=/usr/bin".partition("=")
print(key)
print(val)