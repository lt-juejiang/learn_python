#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
要创建一个class对象，type()函数依次传入3个参数：

1.class的名称；
2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''

def fn(self,name='world'):
    print ('hello %s.' % name)

Hello = type('Hello',(object,),dict(hello=fn))
h=Hello()
h.hello()

