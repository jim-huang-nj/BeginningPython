# -*- coding: utf-8 -*-
# @Time  : 2020/11/18 18:44
# @Author : Jim Huang！！
# @FileName: 1-4.py
# @Software: PyCharm
# 打印一个边长为n的正方形

n = int(input("Please enter one integer:"))
print('*  '*n)
for i in range(n-2):
    print('*  '+'   '*(n-2)+'*')
print('*  '*n)
