'''
Author: Jim Huang
Date: 2022-02-09 17:31:32
LastEditors: Jim Huang
LastEditTime: 2022-02-09 17:37:13
Description: copy file
'''

from xml.sax.xmlreader import InputSource


def copyfile(f1, f2):
    source = open(f1,"r")
    destination = open(f2,"w")
    while insource in source.readline():
        destination.write(insource)
    
    source.close()
    destination.close()

copyfile("5-2-5.py","copyedfile")
    



