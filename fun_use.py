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
            # rel[str(func)[str(func).find('function ') + 9: -1]] = func(num)
            rel[func.__name__] = func(num)

        except ValueError:
            # rel[str(func)[str(func).find('function ') + 9: -1]] = 'None'
            rel[func.__name__] = 'None'
    # 返回结果字典
    return rel

# 函数调用
result = same(-10.5, sqrt, abs, tan)
# 结果输出
print result
'''
运用双层循环求出一个list中各个元素在不同计算方法下的结果
'''
def do_expr(x=[],*kw):
    return(f(x_k) for x_k in x for f in kw)

for n in do_expr([1,4,9,16],sqrt,abs):
    print n
