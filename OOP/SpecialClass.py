#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# class Student(object):
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return 'Student object(name:%s)' % self.name

# s=Student('Michael')
# print s


class Student(object):

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s=Student('Michael')
s()
print callable(s)
print callable(max)
print callable([1, 2, 3])
print '****************************'
class Fib2(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

for n in Fib2():
    print(n)
print '****************************'
class Fib(object):
    def __getitem__(self, item):
        a,b =1,1
        for x in range(item):
            a,b=b,a+b
        return a
f=Fib()
print 'f[3]=',f[3]
print '****************************'
class Fib1(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f1=Fib1()
print 'f1[:5]=',f1[:5]
print '****************************'

class magic():
    ''' 设置路径 %s = 当前类的path值 / %s = 传入的path值 '''
    def __init__(self,path=''):
        self.path=path

    ''' 把类当作变量时候触发的 返回当前类的path变量信息'''
    def __str__(self):
        return self.path

    ''' 调用当前类时候 递归执行__init__设置当前类path变量 '''
    def __call__(self,path):
        return magic(path)

    ''' 调用一个不存在的属性时候 判断是否是指定的属性，返回相对应的函数或递归调用当前类 进行path变量设置 '''
    def __getattr__(self,path):
        return ((lambda u:self(self.path+'/'+u)) if path=='User' else self(self.path+'/'+path))

print(magic().User('知名混混').Accounts.Money)