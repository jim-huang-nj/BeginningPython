'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-03 22:25:26
LastEditors: CoderXZ
LastEditTime: 2021-05-04 11:45:04
'''
# def f(x,y,z):
#     print(x)
#     print(y)
#     print(z)
    
# f(z=None,y=10,x=[1])
# f((1,),z=6,y=4.1)
# f(y=5,z=6,2)

# def add(*nums):
#     sum = 0
#     print(type(nums))
#     for x in nums:
#         sum += x
#     return sum
# print(add(1,3,5))
# print(add([2,4,6]))

def showconfig(**kwargs):
    for k,v in kwargs.items():
        print("{} = {}".format(k,v ))
        
showconfig(host="127.0.0.1",port="8080",username="wayne",password="magedu")