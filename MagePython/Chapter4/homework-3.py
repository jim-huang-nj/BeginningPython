'''
Author: Jim Huang
Date: 2022-01-30 15:10:27
LastEditors: Jim Huang
LastEditTime: 2022-01-30 15:43:40
Description: 公共子串
'''
from itertools import count
from xml.etree.ElementTree import SubElement


s1 = "abcdefg"
s2 = "sefabcdoabcdeftw"
s3 = "1234a"

def findit(str1,str2):
    count = 0
    if len(str2) < len(str1):
        str1, str2 = str2, str1
    length = len(str1)
    for sublen in range(length,0,-1):
        for start in range(0,length-sublen+1):
            substr = str1[start:sublen]
            count +=1
            if str2.find(substr) > -1:
                print("count={},substrlen={}".format(count,sublen))
                return substr

print(findit(s1,s2))
#print(findit(s1,s3))