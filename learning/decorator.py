#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
import time


def log(func):
    def wrapper(*args, **kw):
        print('call %s:' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log  # 相当于 now = log(now)
def now():
    print('2018-5-9')


f = now
f()
print(f.__name__)
print('=================')


# =============================自定义文本============
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s %s(): ' % (text, func.__name__))
            return func(*args, **kw)
        # wrapper.__name__ = func.__name__
        return wrapper
    return decorator


@log2('excute')
def cutime():
    print('15:16')


ff = cutime
ff()
print(ff.__name__)


print(time.strftime("%Y-%m-%d,%H:%M:%S", time.localtime()))
print(time.ctime())
