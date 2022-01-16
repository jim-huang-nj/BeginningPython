# -*- coding: utf-8 -*-
# @Time  : 2020/11/18 17:59
# @Author : Jim Huang！！
# @FileName: 1-1.py
# @Software: PyCharm
# 给定一个不超过5位的正整数，判断其有几位
while True:
    val=input("Please enter one number < 100000:")
    val = int (val)
    if val < 100000:
        break
if val >= 10000:
    print("The length of integer is 5")
elif val >= 1000:
    print("The length of integer is 4")
elif val >= 100:
    print("The length of integer is 3")
elif val >= 10:
    print("The length of integer is 2")
else:
    print("The length of integer is 1")

