# -*- coding: utf-8 -*-
# @Time  : 2020/11/18 18:35
# @Author : Jim Huang！！
# @FileName: 1-3.py
# @Software: PyCharm
# 给定一个不超过5位的正整数，判断该数的位数，依次从万位打印到个位的数字
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
mode=10000
for i in range(5):
    print(int(val//mode))
    #val = val - (val // mode)*mode
    val = val % mode
    mode = mode / 10
