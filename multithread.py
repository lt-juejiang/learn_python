#!/user/bin/python
#coding=utf-8

import time , threading

# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


# balance = 0
# def change_it (n):
#
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     lock = threading.RLock()
#     for i in range(100000):
#          lock.acquire()
#          try:
#              change_it(n)
#          finally:
#              lock.release()
#
# def run_thread(n):
#
#      for i in range(1000000):
#               change_it(n)
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)


# # 创建全局ThreadLocal对象:
# local_school = threading.local()
# def process_student():
#     #获取当前线程关联的student
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))
#
# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()
# t1 = threading.Thread(target=process_thread, args=('Alice',),name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob',),name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()


local = threading.local()

def change_stu(stu):
    stu['age'] += 1

def stu_thread(name, age, class_):
    stu = local.stu = {'name': name, 'age': age, 'class': class_}
    print('当前线程(%s)的local为：%s' % (threading.current_thread().name, local.__dict__))
    change_stu(stu)
    print('当前线程(%s)的local为：%s' % (threading.current_thread().name, local.__dict__))

t1 = threading.Thread(target=stu_thread, args=('Bob', 23, '三（1）'), name='Thread-1')
t2 = threading.Thread(target=stu_thread, args=('Lucy', 21, '三（2）'), name='Thread-2')
t1.start()
t2.start()
t1.join()
t2.join()
print('当前线程(%s)的local为：%s' % (threading.current_thread().name, local.__dict__))

# local = threading.local()
#
# def change_age():
#     stu = local.stu
#     stu['age'] += 1
#
# def stu_thread(name, age, class_):
#     local.stu = {
#         'name': name, 'age': age, 'class': class_
#     }
#     print('当前线程(%s)的local为：%s' % (threading.current_thread().name, local.__dict__))
#     change_age()
#     print('当前线程(%s)的local变为：%s' % (threading.current_thread().name, local.__dict__))
#
# s1 = threading.Thread(target=stu_thread, args=('Bob', 23, '三（1）'), name='Thread-1')
# s2 = threading.Thread(target=stu_thread, args=('Lucy', 21, '三（2）'), name='Thread-2')
# s1.start()
# s2.start()
# s1.join()
# s2.join()
# print('当前线程(%s)的local为：%s' % (threading.current_thread().name, local.__dict__))


