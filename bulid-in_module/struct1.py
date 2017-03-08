#!/user/bin/python
#coding=utf-8
import struct

def readBMP(fi):
    with open(fi, 'rb') as f:
        bita = f.read()
        bit = bita[:30]
    return bit
def judgeBMP(s):
    s1 = struct.unpack('<ccIIIIIIHH', s)
    if s1[0] == b'B' and s1[1] == b'M':
        print('windows')
        print(s1[6], '*', s1[7], '---', s[-1])
    elif s1[0] == b'B' and s1[1] == b'A':
        print('apple')
        print(s1[6],'*',s1[7],'---',s1[-1])
    else:
        print('Is not BMP file!')

if __name__=='__main__':

    tx=readBMP('/Users/liuting/PycharmProjects/learn python/fun_use.py')
    judgeBMP(tx)