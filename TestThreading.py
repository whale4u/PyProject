import threading
import time

n = 5
def xiancheng():
    global n
    while True:
        if n>0:
            mutex.acquire()
            n-=1
            print("线程%s：%d" % (threading.currentThread(), n))
            mutex.release()
            time.sleep(0.1)

mutex = threading.Lock()

t1=threading.Thread(target=xiancheng).start()
t2=threading.Thread(target=xiancheng).start()
t3=threading.Thread(target=xiancheng).start()
