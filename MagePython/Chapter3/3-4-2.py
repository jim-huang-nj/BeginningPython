'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-03 09:09:36
LastEditors: CoderXZ
LastEditTime: 2021-05-03 09:42:45
'''
newlist = [print(i) for i in range(10)]
print(newlist)

a =[i for i in range(20) if i%2 == 0 or i%3 ==0] 
print(a)

#print("{0:2}*{1:2}={2:2}  ".format([(i,j,i*j) for i in range(1,10) for j in range(1,i+1)]))
[print("{0:<2} *{1:2} = {2:<2}  ".format(i,j,i*j),end="\n" if i==j else "" ) for i in range(1,10) for j in range(1,i+1)]