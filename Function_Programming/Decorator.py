#!/user/bin/python
#coding=utf-8
import functools
'''
在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
'''
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)#函数对象有一个__name__属性，可以拿到函数的名字：
        return func(*args, **kw)
    return wrapper

@log
def now():
    print ('2015-3-25')

print now()
print'*********************'

def log1(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():'%(text,func.__name__))#函数对象有一个__name__属性，可以拿到函数的名字：
            return func(*args, **kw)
        return wrapper
    return decorator
@log1('excute')
def now():
    print ('2015-3-25')

print now()

def log2(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return wrapper


print'*********************'
def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log3('excute')
def now():
    print ('2015-3-25')
print now.__name__
print'*********************'
'''
可以同时支持带参数和不带参数的decorator
'''
def log4(text = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            def printLog(s,text = None):
                if text == None:
                    print('%s %s():' % (s,func.__name__))
                else:
                    print('%s %s %s():' % (text,s,func.__name__))
            printLog('before call',text)
            func(*args, **kw)
            printLog('end call',text)
        return wrapper
    return decorator

@log4()
def f1():
    print('f1')

@log4('test')
def f2():
    print('f2')
print f1()
print f2()
print'*********************'
def log5(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('begin call %s():' %func.__name__)
        func(*args,**kw)
        print('end call %s():' %func.__name__)
        # return func(*args,**kw)
    return wrapper
@log5
def f3():
    print 'pass'
print f3()