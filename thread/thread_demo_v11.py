#!/usr/bin/python3
# -*- coding: utf-8 -*-
import threading
import time

'''
Python通过自定义类继承 Thread，然后重写 run() 方法，实现多线程。
'''


class MyThread(threading.Thread):
    def __init__(self, func, arg):
        super(MyThread, self).__init__()
        self.func = func
        self.arg = arg

    def run(self):
        self.func(self.arg)


def do_work(args):
    time.sleep(1)
    print("Task %s finished!" % args)


for each_task in range(5):
    obj = MyThread(do_work, each_task)
    obj.start()

# time.sleep(2)
print("Main thread finished!")