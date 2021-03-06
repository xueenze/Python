import os

print('Process (%s) start...' % os.getpid())

from multiprocessing import Process

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Process(target = run_proc, args = ('test',))
    print('Child process will start.')
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print('Child process end.')