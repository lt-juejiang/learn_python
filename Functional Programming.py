#!/user/bin/python
#coding=utf-8
from functools import reduce
def f(x):
    return x*x

def is_odd(x):
    return x%2==1

def prod(l):
    def product(x,y):
        return x*y
    return reduce(product,l)

def add(x, y):
    return x + y

def integer(x,y):
    return x*10+y
def float(x,y):
    return x*0.1+y

def char2num(s1):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s1]

def str2int(s):
    return reduce(integer,map(char2num,s))

def str2int_o(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

def normalize(name):
    return name[0].upper()+name[1:].lower()

def str2float(str):
    n=str.find('.')
    list1=str[:n]
    list2=str[-1:n:-1]
    return reduce(integer,map(char2num,list1)) + reduce(float,map(char2num,list2))*0.1

def not_empty(s):
    return s and s.strip()

# def _odd_iter():
#     n=1
#     while True:
#         n=n+2
#         yield n
# def _not_divisible(n):
#     return  lambda x:x%n>0
# def primes():
#     yield 2
#     it=_odd_iter()
#     while true:
#         n=next(it)
#         yield n
#         it=filter(_not_divisible(n),it)


'''
map()的用法
'''
l=[1,2,3,4,5,6,7,8,9]
r=map(f,l)
print r
print list(r)
print '*****************'
# print list(map(str,l))
# print '*****************'
'''
reduce()的用法
'''
p=reduce(add, [1, 3, 5, 7, 9])
print p
print '*****************'
print '1*2*3*4 =',prod([1,2,3,4])
print '*****************'
print reduce(integer,[1, 3, 5, 7, 9])
print '*****************'
'''
filter()函数用于过滤序列
'''
print filter(is_odd,[1,2,3,4,5,6,7,8,9])
print '*****************'
print filter(not_empty, ['A', '', 'B', None, 'C', '  '])
print '*****************'
s='123456'
# t= {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s[0]]
# print t

print str2int(s)
print str2int_o(s)
print '*****************'
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
print '*****************'
# print 10**2
print str2float('123.456')
# print '******100内的素数*******'
# for i in primes():
#     if i<10:
#         print i
#     else:
#         break
#
# print '*****************'
# print filter(_not_divisible(3),[1,2,3,4,5,6,7,8,9])