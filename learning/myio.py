#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author: tomsky.wang 
# @Date: 2018-05-11 17:57:53

from io import StringIO, BytesIO
import os

# with open('mydict.py', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())

# f = open('files/bd_logo.png', 'rb')
# print(f.read())
# f.close()

# f = StringIO()
# print(f.write('hello'))
# f.write(' ')
# f.write('world!')
# print(f.getvalue())

f = StringIO('How are you?\nI\'m fine, thank you')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f = BytesIO()
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())

print(os.uname())
print(os.environ.get('TERM'))
