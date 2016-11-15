#!/user/bin/python
#coding=utf-8
'''
#init称为构造函数或者初始程序，初始化类或对象的实例，在这个_init_下，新创立的对象就是self#
'''
# class Student(object):
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#     def print_score(self):
#         print('%s: %s' %(self.name,self.score))
#     def get_grade(self):
#         if self.score>=90:
#             return 'A'
#         elif self.score>=80:
#             return 'B'
#         elif self.score>=60:
#             return 'C'
#         else:
#             return 'D'


# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()
# print bart.get_grade()
# print lisa.get_grade()
# class Student1(object):
#     pass
# ba = Student1()
# print ba
# print Student1
class Student():

    def get_grade(self):
        self.score=54
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'

a=Student()
print a.get_grade()
