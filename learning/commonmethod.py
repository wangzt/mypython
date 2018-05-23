#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author: tomsky.wang 
# @Date: 2018-05-16 11:30:38

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter


Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))

q = deque(['a', 'b', 'c'])
q.append('y')
q.appendleft('x')
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

d = dict([('a,', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict(d)
print(od)

od = OrderedDict()
od['x'] = 1
od['y'] = 2
od['z'] = 3
print(list(od.keys()))

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
