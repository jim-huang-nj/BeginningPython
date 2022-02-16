<<<<<<< HEAD
def add(x,y):
    """This is a function of addition"""
    a = x + y
    return x + y

print("name={}\ndoc={}".format(add.__name__,add.__doc__))
print(help(add))    
=======
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
    



>>>>>>> 329ea65386108fa9d503378ca5524dcf0e92f52a
