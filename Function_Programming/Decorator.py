#!/user/bin/python
#coding=utf-8

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


