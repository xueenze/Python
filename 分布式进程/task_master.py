# _*_ coding:utf-8 _*_
import random, time, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

def get_task():
    return task_queue

def get_result():
    return result_queue

def start_server():
    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d..' % n)
        task.put(n)

    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)

    manager.shutdown()
    print('master exit')

if __name__ == '__main__':
    start_server()