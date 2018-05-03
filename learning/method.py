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


def quadratic(a, b, c):
    if (not isinstance(a, int)) or (not isinstance(b, int))\
         or (not isinstance(c, int)):
        raise TypeError('Please input int type')
    st = math.sqrt(math.pow(b, 2) - 4 * a * c)
    divider = 2 * a
    return (-b + st)/divider, (-b - st)/divider


result = quadratic(1, -4, 1)
print(result)
