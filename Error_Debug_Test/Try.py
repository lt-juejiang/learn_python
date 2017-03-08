#!/user/bin/python
#coding=utf-8

import logging
# err_logging.py

# except ValueError as e:
#     # 处理错误1
#     pass
# except ZeroDivisionError as e:
#     # 处理错误2
#     pass
# except BaseException as e:
#     # 处理所有其他类型错误
#     pass
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
print('************************')
# try:
#     print('try...')
#     r = 10 / 2
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')
# print('************************')
# try:
#     print('try...')
#     r = 10/int('2')
#     print('result',r)
# except ValueError as e:
#     print('ValueError',e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError',e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('end...')
# print('************************')




# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('END')

