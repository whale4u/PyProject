#!/usr/bin/python3
# -*- coding: utf-8 -*-
import threading
import time

'''
互斥锁是一种独占锁，同一时刻只有一个线程可以访问共享的数据。
'''

num = 5
mutex = threading.Lock()


class MyThread(threading.Thread):
    def run(self):
        global num
        # 如果上锁成功
        if mutex.acquire(True):
            num = num-1
            print("num = %s" % num)
            time.sleep(1)
            mutex.release()


for i in range(5):
    t = MyThread()
    t.start()

