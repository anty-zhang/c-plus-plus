# -*- coding: utf-8 -*-

import multiprocessing as mp
import time


def job(v, num):
    for i in range(10):
        time.sleep(0.1)
        v.value += num

        print("v.value: ", v.value)


# 创建多进程 multiprocessing
def multicore():

    v = mp.Value('i', 0)
    thread1 = mp.Process(target=job, args=(v, 1))
    thread2 = mp.Process(target=job, args=(v, 3))

    thread1.start()
    thread2.start()
    thread2.join()
    thread1.join()


if __name__ == '__main__':
    multicore()
