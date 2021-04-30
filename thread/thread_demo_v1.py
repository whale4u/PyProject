#!/usr/bin/python3
# -*- coding: utf-8 -*-
import threading
import time

'''
Python多线程实现传参
'''


def do_work(task_name):
    time.sleep(1)
    print("Task %s finished by %s !" % (task_name, threading.current_thread()))


for each_task in range(5):
    # 这里do_work不能写成do_work()
    thread = threading.Thread(target=do_work, args=(each_task,))
    thread.start()

# time.sleep(0.5)
print("Main thread finished!")
