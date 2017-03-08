#!/user/bin/python
#coding=utf-8

class Student(object):
    @property     #把一个getter方法变成属性
    def score(self):
        return self.__score
    @score.setter  #负责把一个setter方法变成属性赋值
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score=value

s=Student()
s.score=80
print s.score

class Stu(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property  #对age定义只读属性
    def age(self):
        return 2015 - self._birth
x=Stu()
x.birth=1991
print x.birth
print x.age

class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        self.__height = value

    @property
    def resolution(self):
        return self.__width*self.__height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
