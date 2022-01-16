'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-03 11:09:33
LastEditors: CoderXZ
LastEditTime: 2021-05-03 12:37:38
'''
it = (x for x in range(10) if x %2 )
#print(it)
first = next(it)
print(first)
second = next(it)
print(second)
val = first + second
print("val is "+str(val))

third = next(it)
print(third)

for x in enumerate([2,4,6,8]):
    print(x)
    
for  x in enumerate("abcde"):
    print(x,end="")