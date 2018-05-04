#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from collections import Iterable

L = list(range(101))
print(L[1:3])

str1 = 'Hello world  '
size = len(str1)
print(size)
print(str1[6:size])

trimStr = str1.strip()
print(len(trimStr))

str2 = '12 12 345 21 21'
print(str2.strip('12'))

print()
print(isinstance('abc', Iterable))

# c = ('a', 'b', 'c')
# for cc in c:
#     print(cc)

print()
d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, v)

print()
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 列表生成式
print()
L = [x * x for x in range(1, 11)]
print(L)

# 全排列
print()
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

# 目录
print()
L = [d for d in os.listdir('.')]
print(L)
print(len(L[-1]))

# 字符串变小写
print()
L = ['Hello', 'World', 'IBM', 18, 'Apple']
# print(isinstance(L[1], str))
print([s.lower() if isinstance(s, str) else s for s in L])

# 生成器
print()
G = (x * x for x in range(10))
for n in G:
    print(n)

# 斐波那切数列
print()
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        # print(b)
        # t = a
        # a = b
        # b = t + b
        n = n + 1

    # print('done')
    yield 'done'


f = fib(10)
for n in f:
    print(n)


