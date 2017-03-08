#!/user/bin/python
#coding=utf-8
import types
from InheritanceAndPolymorphism import Animal,Dog,Cat

#能用type()判断的基本类型也可以用isinstance()判断
print type(123)
print type(456)
print type('123')
print '************************'
print 'type(123)==type(456):',type(123)==type(456)
print 'type(123)==type(\'123\'):',type(123)==type('123')
print '************************'
print type(abs)
print type(abs)==types.BuiltinFunctionType
print '************************'
animal=Animal()
print isinstance(animal,Animal)
print '************************'
dog=Dog()
print isinstance(dog,Animal)
print '************************'
#如果要获得一个对象的所有属性和方法，可以使用dir()函数
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
myobject=MyObject()
print dir(myobject)
print hasattr(myobject,'x')
setattr(myobject,'y',10)
print hasattr(myobject,'y')
print myobject.y
print getattr(myobject,'y')
print '************************'
class a(object):
    def b(self):
        return
print type(a)
print type(a())
print type(a.b)
print type(a().b)
print '************************'
#判断某个属性是否方法callable()
list=[f for f in dir(myobject) if callable(getattr(myobject,f))]
print(list)
