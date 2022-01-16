'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-04 17:58:45
LastEditors: CoderXZ
LastEditTime: 2021-05-04 23:15:33
'''
import random
def comparenumber(x,y):
    if x > y:
        print("Max number is {}".format(x))
        print("Min number is {}".format(y))
    else:
        print("Max number is {}".format(y))
        print("Min number is {}".format(x))

comparenumber(5,8)

def double_value(*nums):
    print(nums)
    return max(nums),min(nums)

print("Max is {},Min is {}".format( *double_value(*[random.randint(10,20) for _ in range(10)])))