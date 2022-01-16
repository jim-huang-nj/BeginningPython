'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-04 11:47:48
LastEditors: CoderXZ
LastEditTime: 2021-05-04 14:01:53
'''
# def fn(*args,x,y,**kwargs):
#     print(x)
#     print(y)
#     print(args)
#     print(kwargs)
    
# #fn(3,5,7,9,10,a=1,b="python")    
# fn(3,5,y=5,x=3,a=1,b="python")

# def fn(*args,x):
#     print(x)
#     print(args)
    
# fn(3,5,x=7)

# def fn1(x=5,**kwargs):
#     print("x={}".format(x,))
#     print(kwargs)
# fn1(3,y=10)
def add(*iterable):
    result = 0
    for x in iterable:
        result +=x
    return result

print(add(*range(10)))

#print(add(4,5))
#add((4,5))
#t= (4,5)
#print(add(t[0],t[1]))
#print(add(*{4,5}))
# add(*(4,5))
#print(add(*range(1,3)))