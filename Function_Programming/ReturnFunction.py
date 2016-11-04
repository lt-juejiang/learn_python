#!/user/bin/python
#coding=utf-8
def lazy_sum(*args):
    def sum():
        n=0
        for i in args:
            n = n+i
        return n
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print f()
print '********************'
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print f1()
print f2()
print f3()
print '********************'
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1,f2,f3 = count()
print f1()
print f2()
print f3()
print '********************'
f4 = count()
print f4[0]()
print f4[1]()
print f4[2]()
print '********************'
def hellocounter(name):
    count=[0]
    def counter():
        count[0]=count[0]+1
        print ('Hello,',name,',',str(count[0])+' access!')
    return counter
hello = hellocounter('guzhendong')
hello()
hello()
hello()
print '********************'
def co():
    def f(j):
         w=lambda j: (j*j)
         return w(j)
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs
print co()