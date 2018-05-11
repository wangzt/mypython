#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)

try:
    print('try...')
    r = 10 / int('2')
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


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('5')
    except Exception as e:
        logging.exception(e)


main()
print('END')


logging.info('--------last info')
