#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from method import my_abs

print("Hello python")
print('I\'m ok.\n')
print('\\\t\\')
print(r'\\\t\\')
print('''line1
line2
line3''')
print(5 > 3 and 3 > 1)

age = 10
if age >= 18:
    print('adult')
else:
    print('teenager')

a = 20
print(9//3)
print(len('中文'))
print(len('中文'.encode('utf-8')))
print('Hello %s, you have %d.' % ('world', 1000))

print(my_abs(-100))

s = input('birth:')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')


