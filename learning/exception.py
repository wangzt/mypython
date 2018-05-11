#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except UnicodeError as e:
    print('UnicodeError:', e)
except ZeroDivisionError as e:
    print('except:', e)
else:
    print('No error')
finally:
    print('Finally...')
print('END')
print("=========================")


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')
