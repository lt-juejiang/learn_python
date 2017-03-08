#!/user/bin/python
#coding=utf-8
class Student(object):
    # 用于记录已经注册学生数
    student_number = 0

    def __init__(self, name):
        self.name = name


# 注册一个学生:注册必填项名字，选填项利用关键字参数传递。注册完成，学生数+1
def register(name, **kw):
    a = Student(name)
    for k, v in kw.items():
        setattr(a, k, v)
    Student.student_number += 1
    return a
bob = register('Bob', score=90)
ah = register('Ah', age=8)
print 'student_number:',Student.student_number
print 'bob:score=',getattr(bob, 'score')
print 'ah:age=',getattr(ah, 'age')

