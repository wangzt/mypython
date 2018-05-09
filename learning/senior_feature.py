#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from collections import Iterable
from functools import reduce
# import itertools
import  collections

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

def f(x):
    return x * x

L = list(map(f, [1, 2, 3, 4, 5, 6]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2sum(s):
        return DIGITS[s]
    return reduce(fn, map(char2sum, s))


print(str2int('12359'))


def capita(s):
    return s.capitalize()


print(list(map(capita, ('python', 'java', 'swift', 'go'))))


def prod(L):
    def fn(x, y):
        return x * y

    return reduce(fn, L)


print(prod([3, 5, 7, 9]))

temp = '123.45'.split('.')
print(temp[0], temp[1])


def str2float(s):
    def fn1(x, y):
        return x * 10 + y

    def fn2(x, y):
        return x * 0.01 + y * 0.1

    def char2sum(c):
        return DIGITS[c]

    L = s.split('.')
    LL = list(L[1])
    LL.reverse()
    print(LL)
    result = reduce(fn1, map(char2sum, L[0])) + reduce(fn2, map(char2sum, LL))
    print(result)


str2float('123.45')


scientists = ({'name': 'Alan Turing', 'age': 105, 'gender': 'male'},
             {'name': 'Dennis Ritchie', 'age': 76, 'gender': 'male'},
             {'name': 'Ada Lovelace', 'age': 202, 'gender': 'female'},
             {'name': 'Frances E. Allen', 'age': 84, 'gender': 'female'})


def group_by_gender(accumulator, value):
    accumulator[value['gender']].append(value['name'])
    return accumulator


grouped = reduce(group_by_gender, scientists, {'male': [], 'female': []})
# grouped = reduce(group_by_gender, scientists, collections.defaultdict(list))
print(grouped)

# grouped = {item[0]: list(item[1])
#            for item in itertools.groupby(scientists, lambda x: x['gender'])}
# print(grouped)


def not_empty(s):
    return s and s.strip()


L = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(L)
