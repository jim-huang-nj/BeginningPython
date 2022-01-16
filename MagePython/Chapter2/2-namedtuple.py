'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-01 10:09:30
LastEditors: CoderXZ
LastEditTime: 2021-05-01 10:13:19
'''
from collections import namedtuple
Students = namedtuple("Student","name age")
Jim = Students("Jim",20)
print(Jim.name)
print(Jim.age)