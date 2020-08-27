#!/usr/bin/python3
# -*- coding: utf-8 -*-
import threading
import time

'''
Python多线程使用setDaemon(True)把所有的子线程都变成主线程的守护线程。
当主线程结束后，守护子线程也会随之结束（不管是否运行完成），整个程序也跟着退出。
'''


def do_work(task_name):
    time.sleep(5)
    print("Task %s finished by %s !" % (task_name, threading.current_thread()))


for each_task in range(5):
    # 这里do_work不能写成do_work()
    thread = threading.Thread(target=do_work, args=(each_task,))
    # 把子线程设置为守护线程，必须在start()之前设置
    thread.setDaemon(True)
    thread.start()


print("Main thread finished!")
# 输出活跃的线程数
print(threading.active_count())