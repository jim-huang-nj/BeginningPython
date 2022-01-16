# -*- coding: utf-8 -*-
# @Time  : 2020/11/18 20:21
# @Author : Jim Huang！！
# @FileName: 1-9.py
# @Software: PyCharm
# 求100以内斐波那契数列
a = 0
b = 1
print(str(a)+","+str(b),end="")
while True:
    c = a + b
    if c > 100:
        break
    print(","+str(c),end="")
    a = b
    b = c

