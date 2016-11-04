#!/user/bin/python
#coding=utf-8

'''
关键字lambda表示匿名函数，冒号前面的x表示函数参数
'''
def count():
    f = lambda j:lambda :j*j
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
print '************************'
'''
# （1）、如果你定义一个有参数的函数，返回函数是一个无参函数，
# 那么将定义的有参函数赋值给一个变量(赋值后变量指针指向函数，这时变量就是函数的别名)时，
# 需要转递参数，调用函数变量就等于执行函数体
# （2）、如果你定义一个无参数的函数，返回函数是一个有参函数，
# 那么将定义的无参函数赋值给一个变量(赋值后变量指针指向函数，这时变量就是函数的别名)时，
# 不需要转递参数，调用函数变量时传递参数就等于执行函数体

'''
def build_return_func(x,y):
    def g():
        return x**2+y**2
    return g

def build_return_lambda(x,y):
    return lambda :x**2+y**2
'''
有函数调用
'''
f1=build_return_func(1,2)
f2=build_return_lambda(2,4)
print f1()
print f2()
print '************************'
def build_return_func1():
    def g(x,y):
        return x**2+y**2
    return g
def build_return_lambda1():
    return lambda x,y:x**2+y**2
'''
无函数调用
'''
f3=build_return_func1()
f4=build_return_lambda1()
print f3(1,2)
print f4(2,4)
print '************************'
def build(x,y):
    return lambda a,b: a*a+b*b
f = build(1,2)
print f(3,4)

ff = build('a','b')
print ff(1,2)
