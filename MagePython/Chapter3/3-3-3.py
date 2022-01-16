'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-03 06:12:29
LastEditors: CoderXZ
LastEditTime: 2021-05-03 06:25:10
用户输入一个数字
-打印每一位数字及其重复的次数
'''
d = dict()
while (True):
    a=(int(input("Please input the integer(0 will quit):")))
    if a==0:
        break   
    if a not in d.keys():
        d[a]=0
    d[a]=d[a]+1
for k,v in d.items():
    print("The number '{0}' repeated {1} times.".format(k,v))
    

