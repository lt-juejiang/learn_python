#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
t=isinstance(d, Iterable)
if t:
    print t
    for key in d:
        print key
    print('***********************')
    for value in d.values():
        print (value)
    print('***********************')
    for key,value in d.items():
        print (key,value)
print('***********************')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
print('***********************')
for x in [(1,1),(2,4),(3,9)]:
    print(x)
print('***********************')

for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)
print('***********************')

####Python内置的enumerate函数可以把一个list变成索引-元素对####

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)