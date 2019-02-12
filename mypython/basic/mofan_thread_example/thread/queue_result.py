# -*- coding: utf-8 -*-
"""
store multi threaded result using queue
"""
import threading
import time
from queue import Queue


def job(data_list, result_queue):
    for i in range(len(data_list)):
        data_list[i] = data_list[i] * data_list[i]
    result_queue.put(data_list)


def multithreading():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9]]
    # 对于资源，加锁是个重要的环节。因为python原生的list, dict等，都是not
    # thread safe的。而Queue，是线程安全的，因此在满足使用条件下，建议使用队列
    q = Queue()
    thread_list = []
    for i in range(len(data_list)):
        thread = threading.Thread(target=job, args=(data_list[i], q), name="job_%d" % i)
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        thread.join()

    result_list = []

    for _ in range(len(data_list)):
        result_list.append(q.get())

    print("result=", result_list)

if __name__ == '__main__':
    multithreading()

