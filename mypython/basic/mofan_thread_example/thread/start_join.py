# -*- coding: utf-8 -*-
"""
start and join fun
"""
import threading
import time


def basic_func():
    print("threading.active_count()=", threading.active_count())    # 获取已经激活的线程数
    print("look all threads=", threading.enumerate())               # 查看所有的线程信息
    print("This is a thread of %s" % threading.current_thread())    # 查看当前线程


def thread_job1():
    print("job1 start\n")
    for i in range(10):
        time.sleep(0.1)

    print("job1 finish\n")


def thread_job2():
    print("job2 start\n")
    print("job2 finish\n")


def main():
    thread1 = threading.Thread(target=thread_job1(), name="job1")   # 定义线程
    thread2 = threading.Thread(target=thread_job2(), name="job2")

    # 但为了规避不必要的麻烦，推荐如下这种1221的V型排布
    thread1.start()     # 启动线程
    thread2.start()

    thread2.join()
    thread1.join()      # 阻塞线程

    print("all done\n")

if __name__ == "__main__":
    # basic_func()
    main()
