'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-02 22:39:23
LastEditors: CoderXZ
LastEditTime: 2021-05-03 05:41:01
'''
import random
from collections import defaultdict
d =  {1:"A",2:"B",3:"c"}
for k in d:
    print(d.get(k))
    
for v in d.values():
    print(v)
    
for item in d.items():
    print(item)

for item in d.items():
    print(item[0],item[1])
    
d = dict(a=1,b=2,c='abc')
while len(d):
    print(d.popitem())


d1 = {}
for k in "abcdef":
    for i in range(random.randint(1,5)):
        if k not in d1.keys():
            d1[k] = []
        d1[k].append(i)
print(d1)
        
        
d2 = defaultdict(list)        
for k  in 'abcdef':
    for i in range(random.randint(1,5)):
        d2[k].append(i)
print(d1)