#!/usr/bin/python
#coding=utf-8
from generator import fib
f = abs
print f(-10)
print '***********************'

def add(x,y,f):
    return f(x)+f(y)

print add(-5,6,abs)
print '***********************'

def test_fib(n,f):
    for i in f(n):
        print i

test_fib(5,fib)

#!/usr/bin/python
# -*- coding: utf-8 -*-
# 引入数学模块中的方法
from math import sqrt
from math import tan

'''
高阶函数应用，返回一个数字不同方法计算结果
'''
def same(num, *kw):
    # 参数检查
    if not isinstance(num, (int, float)):
        raise TypeError('bad operand type')

    # 初始化结果字典
    rel = {}
    # 循环计算可变参数
    for func in kw:
        try:
            rel[str(func)[str(func).find('function ') + 9: -1]] = func(num)
        except ValueError:
            rel[str(func)[str(func).find('function ') + 9: -1]] = 'None'
    # 返回结果字典
    return rel

# 函数调用
result = same(-10.5, sqrt, abs, tan)
# 结果输出
print result