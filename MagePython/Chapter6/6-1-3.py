'''
Author: Jim Huang
Date: 2022-02-16 13:51:37
LastEditors: Jim Huang
LastEditTime: 2022-02-16 14:14:50
Description: 请填写简介
'''
f = open("readme.txt")
for line in f:
    print(line,end="")
f.close()
