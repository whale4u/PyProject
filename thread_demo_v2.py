#!/usr/bin/python3
# -*- coding: utf-8 -*-
import threading
import time

'''
Python多线程实现传参，实现线程阻塞，等其它线程结束后主线程才结束。
'''


def do_work(task_name):
    time.sleep(1)
    print("Task %s finished by %s !" % (task_name, threading.current_thread()))


for each_task in range(5):
    # 这里do_work不能写成do_work()
    thread = threading.Thread(target=do_work, args=(each_task,))
    thread.start()
    # 调用该方法将会使主调线(!!!)程堵塞，直到被调用线程运行结束或超时。
    thread.join()

print("Main thread finished!")