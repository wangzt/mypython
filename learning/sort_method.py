#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = sorted([36, 5, -12, 9, -21], key=abs)
print(L)

L = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(L)


def by_score(t):
    return t[1]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
LL = sorted(L, key=by_score, reverse=True)
print(LL)
