'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-03 10:43:14
LastEditors: CoderXZ
LastEditTime: 2021-05-03 11:06:02
'''
g = ("{:04}".format(i) for i in range(1,11))
#next(g)
for x in g:
    print(x)
    
print("====================================")
for x in g:
    print(x)
 

it = (print("{}".format(i+1)) for i in range(2))

print(it)
print("hello")    
first = next(it)
#print(first)
second = next(it)
#print(second)
val = first + second

print(val)