#!/user/bin/python
#coding=utf-8

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_level(self):
        if self.score>=90:
            return self.name + ':A'
        elif self.score>=70:
            return self.name + ':B'
        elif self.score>=60:
            return self.name + ':C'
        else:
            return self.name + ':D'

lisa = Student('lisa',18,91)
jerry = Student('jerry',18,85)
tom = Student('tom',18,45)
print(lisa.get_level())
print(jerry.get_level())
print(tom.get_level())
