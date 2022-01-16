'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-01 15:16:28
LastEditors: CoderXZ
LastEditTime: 2021-05-01 15:19:45
'''
str1 = "黄健"
a=str1.encode("UTF-8")
print(a)
print(a.decode(encoding="utf-8",errors="strict"))