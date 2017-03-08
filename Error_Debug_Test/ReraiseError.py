#!/user/bin/python
#coding=utf-8
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: {}'.format(s))
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise                 ###发生错误后外层exception直接捕获，有空raise，则往上丢错误，即往内层丢，无空raise,则不会


bar()