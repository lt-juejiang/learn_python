#!/user/bin/python
#coding=utf-8


from types import MethodType

# case1 :限制类的属性，对类进行动态添加方法
def set_age(self,age):
    self.age=age
class Student(object):
    __slots__ = ('name', 'score', 'set_age')#__slots__变量，来限制该class实例能添加的属性
    pass
#age并不是类属性，set_age可以理解为给Student添加了一个类方法，Student使用一个指针指向这个方法所在的内存，age也就在这个内存块中，它们都不在Student所在的内存块中
Student.set_age=MethodType(set_age,Student)
# s=Student()
# s.set_age()
# print(s.age)
s1 = Student()
s2 = Student()

s1.set_age(15)
print s1.age
print id(s1.age)
s2.set_age(20)
print s1.age
print id(s1.age)
print id(s2.age)
print(s1.age, s2.age, Student.age)
#…………………………………………………………


# case2 :限制类的属性，对实例进行动态添加方法

# s=Student()
# s.set_age=MethodType(set_age,s)
# s.set_age()
# print s.age

#…………………………………………………………
# def print_name(self):
#     print(self.name)
#
#
# class A(object):
#     text = 'A'
#     def __init__(self, name):
#         self.name = name
#
# A.print_name = MethodType(print_name, A)
# a = A('a')
# a.print_name()

def print_name(self, a):
    if isinstance(a,type(self)):
        print(self.text)
    else:
        print(a.name)


class A(object):
    text = 'A'
    def __init__(self, name):
        self.name = name

A.print_name = MethodType(print_name, A)
a = A('a')
b = A('b')
a.print_name(A)
b.print_name(a)
A.print_name(b)
