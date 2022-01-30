'''
Author: Jim Huang
Date: 2022-01-30 10:17:04
LastEditors: Jim Huang
LastEditTime: 2022-01-30 10:50:21
Description: base64 
'''


alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64encode(src:str):
    ret = bytearray()
    if isinstance(src,str):
        _src = src.encode()
    else:
        return

    length = len(_src)
    
    #r 记录补0 的个数
    r =0
    for offset in range(0,length,3):
        triple = _src[offset:offset+3]
        if offset +3 > length:
            r = 3 - len(triple)
            triple += b'\x00'*r
            b = int.from_bytes(triple,"big")
            for i in range(18,-1,-6):
                if i == 18:
                    index = b >> i
                else:
                    index = b >> i & 0x3F
                ret.append(alphabet[index])
    if r:
        ret[-r:] = b"="*r
    return bytes(ret)


import base64

strlist = ["a","`","ab","abc","abcd","ManMa","教育a"]
for x in strlist:
    print(x)
    print(base64encode(x))
    print(base64.b64encode(x.encode()))
    print()