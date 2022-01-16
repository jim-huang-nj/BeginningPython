'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-02 11:06:24
LastEditors: CoderXZ
LastEditTime: 2021-05-02 12:29:41
随机产生2组各10个数字的列表，如下要求：
-每个数字取值范围[10,20]?统计20个数字中，一共有多少个不同的数字？
-2组之间进行比较，不重复的数字有几个？分别是什么？
-2组之间进行比较，重复的数字有几个？分别是什么
'''
import random
lst1=[]
lst2=[]
set1=set()
set2 = set()
total_set = set()
for _ in range(10):
    randnumber = random.randint(10,20)
    lst1.append(randnumber)
    set1.add(randnumber)
    total_set.add(randnumber)
for _ in range(10):
    randnumber = random.randint(10,20)
    lst2.append(randnumber)
    set2.add(randnumber)
    total_set.add(randnumber)
set3 = set1 ^ set2
set4 = set1 & set2
print( "Group1 is {}".format(lst1))
print( "Group2 is {}".format(lst2))
print("Total different number has {0}".format(len(total_set)))
print("Between 2 groups, different number hav {0},they are {1}".format(len(set3),set3))
print("Between 2 groups, same number hav {0},they are {1}".format(len(set4),set4))