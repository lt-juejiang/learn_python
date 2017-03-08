#!/user/bin/python
#coding=utf-8
import random, time, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManger(BaseManager):
    pass

QueueManger.register('get_task_queue', callable=lambda: task_queue)
QueueManger.register('get_result_queue', callable=lambda: result_queue)

manager = QueueManger(address=('', 5000), authkey= b'abc')

manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = random.randint(0, 10000)
    print('put task %d...' % n)
    task.put(n)
print('Try get result...')

for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)

manager.shutdown()
print('master exit.')

