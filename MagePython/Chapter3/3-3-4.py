'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-03 06:26:29
LastEditors: CoderXZ
LastEditTime: 2021-05-03 06:48:42
数字重复统计
-随机产生100个整数
数字的范围[-1000, 1000]
-升序输出这些数字并打印其重复的次数
'''
import random
lst = list()
set1 = set()
d = dict()
for _ in range(100):
    a = random.randint(-1000,1000)
    lst.append(a)
    set1.add(a)
    if a not in d.keys():
        d[a]=0
    d[a]+=1
odlst=list(set1)
odlst.sort()
print("Number  repeated times")
for i in odlst:
    print("{0:<9}{1}".format(i,d[i]))

