# -*- coding: utf-8 -*-
# @Time  : 2020/11/18 20:09
# @Author : Jim Huang！！
# @FileName: 1-8.py
# @Software: PyCharm
# 打印闪电
for i in range(-3,4):
    if i ==0:
        star=7
    else:
        star=4-abs(i)
    if i <=0:
        print(" "*abs(i)+"*"*star)
    else:
        print(" "*3+"*"*star)
