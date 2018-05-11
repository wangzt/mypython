#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('Bar Simpson', 59)
lisa = Student('Lisa Simpson', 78)
bart.print_score()

bart.age = 8
print(bart.age)

print(type(123) == int)


def fn():
    pass


print(type(fn))
print(type(abs))
print(type(lambda x: x))


print(hasattr(bart, 'name'))
setattr(bart, 'x', 19)
print(hasattr(bart, 'x'))


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数a,b
    
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:  # 退出条件
            raise StopIteration()
        return self.a  # 返回下一个值


# n = Fib()
# print(next(n))
# print(next(n))
# print(next(n))
for n in Fib():
    print(n)

