#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# g = (x * x for x in range(10))
# print g
# for i in g:
#     print i
#
# print '***********************'


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# print fib(5)
# print '***********************'

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
# for i in fib(5):
#     print i
# a, b = b, a + b
# 相当于：
#
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]
