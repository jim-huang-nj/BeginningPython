'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-03 06:50:51
LastEditors: CoderXZ
LastEditTime: 2021-05-03 07:15:21
字符串重复统计
字符表'abcdefghijklmnopqrstuvwxyz'
随机挑选2个字母组成字符串，共挑选100个降序输出所有不同的字符串及重复的次数
'''
import random
lst=list('abcdefghijklmnopqrstuvwxyz')
set1= set()
d = dict()
for _ in range(100):
    sample = random.sample(lst,2)
    str1 = sample[0]+sample[1]
    set1.add(str1)
    if str1 not in d.keys():
        d[str1]=0
    d[str1]+=1
lst1 = list(set1)
lst1.sort(reverse=True)
for i in lst1:
    print("{0}   {1}".format(i,d[i]))