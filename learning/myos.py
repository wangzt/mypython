#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from multiprocessing import Process

# print('Process (%s) start...' % os.getpid())

# pid = os.fork()  # fork调用会返回两次，第一次返回非零值
# print(pid)

# if pid == 0:
#     print('I am child process (%s) and my parent is (%s).' % (os.getpid(),
#         os.getppid()))
# else:
#     print('I (%s) just create a process (%s)' % (os.getpid(), pid))


def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

