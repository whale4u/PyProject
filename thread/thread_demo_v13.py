#!/usr/bin/python3
# -*- coding: utf-8 -*-
import threading
import time

'''
Python通过自定义类继承 Thread，然后重写 run() 方法，实现多线程。
并使用setDaemon(True)把所有的子线程都变成主线程的守护线程。
当主线程结束后，守护子线程也会随之结束（不管是否运行完成），整个程序也跟着退出。
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
    # 把子线程设置为守护线程，必须在start()之前设置
    obj.setDaemon(True)
    obj.start()


print("Main thread finished!")
# 输出活跃的线程数
print(threading.active_count())