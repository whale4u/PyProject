#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

"""
装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。
装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。
概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
"""


def timeit(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('used:', end - start)
    return wrapper


@timeit
def foo():
    print('in foo()')


foo()