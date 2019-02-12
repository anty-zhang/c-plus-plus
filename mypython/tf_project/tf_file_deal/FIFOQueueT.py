# -*- coding: utf-8 -*-
# TensorFlow中队列机制
# reference: https://www.cnblogs.com/zyly/p/8982335.html
# http://www.yyliu.cn/post/89458415.html
# https://zhuanlan.zhihu.com/p/27238630

import tensorflow as tf
import threading, time


def test1():
    """
    入队操作在主线程中完成
    创建一个先进先出队列，出队+1，然后在入队操作
    """
    q = tf.FIFOQueue(3, 'float')

    init = q.enqueue_many(([0.1, 0.2, 0.3],))

    x = q.dequeue()

    y = x + 1

    q_inc = q.enqueue([y])

    with tf.Session() as s:
        print(s.run(init))

        for i in range(2):
            s.run(q_inc)

        queue_len = s.run(q.size())

        print("queue len: ", queue_len)

        for i in range(queue_len):
            print("i = ", i, "dequeue =", s.run(q.dequeue()))


def queue_runner():
    """
    入队在多个子线程中完成
    :return:
    """
    q = tf.FIFOQueue(10, 'float')

    # 计数器
    counter = tf.Variable(0.0)
    # 计数器 + 1
    increment_op = tf.assign_add(counter, 1.0)
    # 将计数器入队列
    enqueue_op = q.enqueue(increment_op)

    # 创建QueueRanner
    # 使用多个线程向队列添加数据
    # 创建了4个线程，两个增加计数，两个执行入队
    qr = tf.train.QueueRunner(q, enqueue_ops=[increment_op, enqueue_op] * 2)

    """
    主线程关闭会报错：ERROR:tensorflow:Exception in QueueRunner: Session has been closed.

    # 主线程
    with tf.Session() as s:
        s.run(tf.initialize_all_variables())

        # 启动线程队列
        enqueue_threads = qr.create_threads(s, start=True)

        # 主线程出队
        for i in range(10):
            print(s.run(q.dequeue()))

    """
    # 主线程不关闭的情况
    sess = tf.Session()
    sess.run(tf.initialize_all_variables())

    # 启动入队队列
    qr.create_threads(sess, start=True)
    for i in range(10):
        print(sess.run(q.dequeue()))

    """
    result:
    54.0
    129.0
    189.0
    327.0
    441.0
    514.0
    579.0
    647.0
    720.0
    779.0
    不使用with tf.Session,那么Session就不会自动关闭。

    并不是我们设想的1,2,3,4,本质原因是增加计数的进程会不停的后台运行，执行入队的进程会先执行10次
    （因为队列长度只有10），然后主线程开始消费数据，当一部分数据消费被后，入队的进程又会开始执行。
    最终主线程消费完10个数据后停止，但其他线程继续运行，程序不会结束。

    经验：因为tensorflow是在图上进行计算，要驱动一张图进行计算，必须要送入数据，如果说数据没有送进去，
    那么sess.run()，就无法执行，tf也不会主动报错，提示没有数据送进去，其实tf也不能主动报错，因为tf的训练过程和
    读取数据的过程其实是异步的。tf会一直挂起，等待数据准备好。现象就是tf的程序不报错，但是一直不动，跟挂起类似

    """


def coordinator_test():
    """
    Coordinator是个用来保存线程组运行状态的协调器对象，它和TensorFlow的Queue没有必然关系，是可以单独和Python线程使用的
    将这个程序运行起来，会发现所有的子线程执行完两个周期后都会停止，主线程会等待所有子线程都停止后结束，从而使整个程序结束。由此可见，
    只要有任何一个线程调用了Coordinator的request_stop方法，所有的线程都可以通过should_stop方法感知并停止当前线程
    :return:
    """
    # 子线程函数
    def loop(v_coord, v_id):
        t = 0
        while not v_coord.should_stop():
            print("id=", v_id)
            time.sleep(1)
            t += 1
            # 只有1号线程调用request_stop方法
            if t >= 2 and v_id == 0:
                v_coord.request_stop()

    # 主线程
    coord = tf.train.Coordinator()
    # 调用python API创建10个线程
    threads = [threading.Thread(target=loop, args=(coord, i)) for i in range(10)]

    # 启动所有线程，并等待结束
    for tr in threads:
        tr.start()

    coord.join(threads)

if __name__ == "__main__":
    # test1()
    # queue_runner()
    coordinator_test()
