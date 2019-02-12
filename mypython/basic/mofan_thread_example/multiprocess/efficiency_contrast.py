# -*- coding: utf-8 -*-

import multiprocessing as mp
import threading
import time
from queue import Queue


def job(q):
    res = 0
    for i in range(100000000):
        res += i + i ** 2 + i ** 3

    q.put(res)  # queue


# 创建多进程 multiprocessing
def multicore():
    q = mp.Queue()
    thread1 = mp.Process(target=job, args=(q, ))
    thread2 = mp.Process(target=job, args=(q, ))

    thread1.start()
    thread2.start()
    thread2.join()
    thread1.join()

    print("multicore res=", q.get() + q.get())


# 创建多线程 multithread
def multithread():
    q = Queue()
    thread1 = threading.Thread(target=job, args=(q, ))
    thread2 = threading.Thread(target=job, args=(q, ))

    thread1.start()
    thread2.start()
    thread2.join()
    thread1.join()

    print("multithread res=", q.get() + q.get())


# 创建普通函数
def normal():
    res = 0
    for _ in range(2):
        for i in range(100000000):
            res += i + i ** 2 + i ** 3

    print("normal res=", res)


if __name__ == '__main__':
    st = time.time()
    multithread()
    multithread_end_time = time.time()
    print("multithread cost time=", multithread_end_time - st)

    normal()
    normal_end_time = time.time()
    print("normal cost time=", normal_end_time - multithread_end_time)

    multicore()
    print("multicore cost time=", time.time() - normal_end_time)

    """
    multithread res= 49999999666666671666666600000000
    multithread cost time= 141.29911494255066
    normal res= 49999999666666671666666600000000
    normal cost time= 149.92860102653503
    multicore res= 49999999666666671666666600000000
    multicore cost time= 92.33172821998596
    """
