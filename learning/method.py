#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(9))


def nop():
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


r = move(100, 100, 60, math.pi / 6)
print(r[0])


# Oneline doc string
def quadratic(a, b, c):
    
    if (not isinstance(a, int)) or (not isinstance(b, int))\
         or (not isinstance(c, int)):
        raise TypeError('Please input int type')
    st = math.sqrt(math.pow(b, 2) - 4 * a * c)
    divider = 2 * a
    return (-b + st)/divider, (-b - st)/divider


result = quadratic(1, -4, 1)
print(result)


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end(['Start']))


def cal(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(cal(1, 2, 3))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 20, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Tom', 34, **extra)
