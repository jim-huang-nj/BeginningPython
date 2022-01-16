# -*- coding: utf-8 -*-
# @Time  : 2020/11/18 20:31
# @Author : Jim Huang！！
# @FileName: 1-11.py
# @Software: PyCharm
# 十万以内所有素数
count = 1
for i in range(3,100000,2):
    flag = True
    for j in  range(2,int((i+1)/2)+1):
        if i % j ==0:
            flag = False
            break
    if flag == True:
        count+=1
print(count)