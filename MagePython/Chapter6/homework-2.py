'''
Author: Jim Huang
Date: 2022-02-17 09:07:04
LastEditors: Jim Huang
LastEditTime: 2022-02-17 14:27:44
Description: 统计
'''
from enum import EnumMeta
import re


def makekey(s:str):
    sepcialchars = set(r"""!'"#.,/\()[]*-{}=;:|_%<>^""")
    key = s.lower()
    ret = []
    for i,c in enumerate(key):
        if c in sepcialchars:
            ret.append(" ")
        else:
            ret.append(c)
    return "".join(ret).split()

filename = "sample.txt"
d = {}
with open(filename,encoding="gbk") as f:
    for line in f:
        line1 = line.replace(r"\n","")
        words = line1.split()
        for wordlist in map(makekey,words):
            for word in wordlist:
                d[word] = d.get(word,0) +1
print(type(d))
for k,v in sorted(d.items(),key=lambda item: item[1], reverse=True):
    print(k,v)