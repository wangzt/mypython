#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author: tomsky.wang 
# @Date: 2018-05-16 14:53:12

from urllib import request

with request.urlopen('https://www.baidu.com') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('===========================')
    print("Data:", data.decode('utf-8'))
