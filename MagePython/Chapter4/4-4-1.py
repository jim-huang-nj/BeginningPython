'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-08 21:19:46
LastEditors: CoderXZ
LastEditTime: 2021-05-08 21:37:42
'''
# print((lambda :0)())
# print((lambda x,y=3:x+y)(5))
# print((lambda x,y=3:x+y)(5,6))
# print((lambda x,*,y=30:x+y)(5))
# print((lambda x,*,y=30:x+y)(5,y=10))
# print((lambda *args:(x for x in args))(*range(5)))
print((lambda *args:[x+1 for x in args])(*range(5)))
# print((lambda *args:{x+2 for x in args})(*range(5)))

#[x for x in (lambda *args: map(lambda x:x=1,args))(*range(5))]