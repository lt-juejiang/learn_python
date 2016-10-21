#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
###生成1-10的平方数列＃＃＃
L=[x*x for x in range(1,11)]
print L
###生成1-10的平方偶数数列＃＃＃
L=[x*x for x in range(1,11) if x%2==0]
print L
###使用两层循环，可以生成全排列###
L=[m+n for m in 'ABC'for n in'123']
print L
###列出当前目录下的所有文件和目录名###
L=[d for d in os.listdir('.')]
print L
###列表生成式也可以使用两个变量来生成list###
d = {'x': 'A', 'y': 'B', 'z': 'C' }
L=[k+'='+v for k,v in d.items()]
print L
###把一个list中所有的字符串变成小写###
L = ['Hello', 'World', 'IBM', 'Apple']
L1 = [s.lower() for s in L]
print L1
L2 = ['Hello', 'World', 18, 'Apple', None]
###排除非字符串的元素###
L3 = [s.lower() for s in L2 if isinstance(s,str)]
print L3
