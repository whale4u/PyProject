#!/usr/bin/python3
# -*- coding: utf-8 -*-
import threading
import time

'''
Python通过自定义类继承 Thread，然后重写 run() 方法，实现多线程。
并且实现线程阻塞，等待其它线程结束后主线程才结束。
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
    # 调用该方法将会使主调线(!!!)程堵塞，直到被调用线程运行结束或超时。
    obj.join()

print("Main thread finished!")