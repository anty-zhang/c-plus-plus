import threading
from queue import Queue
import copy
import time


def job(l, q):
    res = sum(l)
    q.put(res)


def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)


def normal(l):
    total = sum(l)
    print(total)


if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)
    print('normal: ', time.time()-s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading: ', time.time()-s_t)

"""
如果你成功运行整套程序, 你大概会有这样的输出. 我们的运算结果没错, 所以程序 threading 和 Normal 运行了一样多次的运算. 但是我们发现
threading 却没有快多少, 按理来说, 我们预期会要快3-4倍, 因为有建立4个线程, 但是并没有. 这就是其中的 GIL 在作怪

1999998000000
normal:  0.08749890327453613
1999998000000
multithreading:  0.05724310874938965
"""