# -*- coding: utf-8 -*-

import multiprocessing as mp
import time


def job(x):
    return x * x


# 创建多进程 multiprocessing
def multicore():
    pool = mp.Pool(processes=2)     # 自定义核的数量
    res = pool.map(job, range(10))  # pool 自己分配数据到进程中
    # res = pool.starmap(job, range(10))
    print("res: ", res)

    # apply_async() 中只能传递一个值，它只会放入一个核进行运算
    # 但是传入值时要注意是可迭代的，所以在传入值后需要加逗号, 同时需要用get()方法获取返回值
    async_res = pool.apply_async(job, (2, ))
    print("async_res: ", async_res.get())

    # 输出多个结果
    async_multi_res = [pool.apply_async(job, (i, )) for i in range(10)]
    print([res.get() for res in async_multi_res])
    pool.close()           # 一定注意需要close pool


if __name__ == '__main__':
    multicore()

