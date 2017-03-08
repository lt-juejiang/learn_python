#!/user/bin/python
#coding=utf-8

# class Student(object):
#     def __init__(self,name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score
#     def get_level(self):
#         if self.score>=90:
#             return self.name + ':A'
#         elif self.score>=70:
#             return self.name + ':B'
#         elif self.score>=60:
#             return self.name + ':C'
#         else:
#             return self.name + ':D'
#
# lisa = Student('lisa',18,91)
# jerry = Student('jerry',18,85)
# tom = Student('tom',18,45)
# print(lisa.get_level())
# print(jerry.get_level())
# print(tom.get_level())

# class Student(object):
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#     def get_score(self):
#         if self.score>=90:
#             return '优良'
#         elif self.score>=60:
#             return '及格'
#         else:
#             return '不及格'
#     def print_score(self):
#         print ('%s:%d-%s' %(self.name,self.score,self.get_score()))
#
# n1 = Student('xiaoling',95)
# n2 = Student('xiaoyang',63)
# n3 = Student('vforbox ',50)
# n1.print_score()
# # Student.print_score(n1)
# n2.print_score()
# n3.print_score()
class Person(object):
    def __init__(self,name,score):
        self.__name = name#__开头的变量是private变量，外部不能直接访问
        self.__score = score
    def func(self):
        print(self.__name)
    def get_name(self):
        return self.__name
#Student类是Person类的子类
class Student(Person):
    def func1(self):
        print(self.get_name())#一个类的私有变量只能在该类被调用，但是，在别的类可以通过调用父类的函数来使用父类的私有变量
    pass

bart = Student('bart',100)
bart.func1()



