# -*- coding: utf-8 -*-
# @Time  : 2020/11/18 20:27
# @Author : Jim Huang！！
# @FileName: 1-10.py
# @Software: PyCharm
# 求内斐波那契数列101项
a = 0
b = 1
print(str(a)+","+str(b),end="")
for i in range(2,102):
    c = a + b
    print(","+str(c),end="")
    a = b
    b = c