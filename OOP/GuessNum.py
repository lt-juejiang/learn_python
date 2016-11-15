#!/user/bin/python
#coding=utf-8

from random import randint
import functools

suiji = [s for s in [randint(1,10) for s in range(1)]]#用randint(1,10)随机生成一个1到10的数,随机1次使用range(1)
# test = [randint(1,10) for s in range(2)]用randint(1,10)随机生成一个1到10的数,随机2次使用range(2)
# print test
class Guess:

    def __init__(self,num=1):
        self.num = num

    def print_guess(self):
        if self.num >= 11 or self.num <= 0:
            print("不得大于11 小于0")
        else:
            print("您猜的数字是：%d" % (self.num))


def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("Welcome to Guess!")
        print("please you random writer one number,but can't exceed 10 and less than 0")
        i = func(*args,**kw)
    return wrapper

@log
def data():
    i = Guess(int(input("请输入：")))
    i.print_guess()
    for x in suiji:
        print("random is %s" % x)
        if i.num == x:
            print("Guess！！")
        else:
            print("No Guess.")


data()
