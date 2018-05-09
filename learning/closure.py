#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count():
    def f(j):
        def g():
            return j * j
        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
print('===================')


def createCounter():
    c = [0]
    def counter():
        c[0] = c[0] + 1
        return c[0]
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA())
