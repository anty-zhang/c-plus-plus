# -*- coding: utf-8 -*-

import tensorflow as tf


def fn(a, b):
    print("a=", a)
    print("b=", b)
    return b + a

# 初始化必须用tf的方式，否则会报错
# elems = [i for i in range(0, 10)] # error
# elems = [1, 2, 3, 4, 5, 6] # error
elems = tf.range(1, 7, dtype=tf.int32)

sum1 = tf.foldl(fn, elems, initializer=0)
sum2 = tf.foldl(fn, elems, initializer=10)
sum3 = tf.foldl(lambda a, b: a + b, elems, initializer=0)

with tf.Session() as sess:
    print("method one")
    print("elems = ", sess.run(elems))
    print("initializer=0 sum1 result=", sess.run(sum1))
    print("initializer=10 sum2 result=", sess.run(sum2))
    print("initializer=0 sum3 result=", sess.run(sum3))


"""
result:
/Users/didi/anaconda3/envs/tf/bin/python /Users/didi/didi/work/tf_example/func/foldl_t.py
/Users/didi/anaconda3/envs/tf/lib/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88
  return f(*args, **kwds)
/Users/didi/anaconda3/envs/tf/lib/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88
  return f(*args, **kwds)
a= Tensor("foldl/while/Identity_1:0", shape=(), dtype=int32)
b= Tensor("foldl/while/TensorArrayReadV3:0", shape=(), dtype=int32)
a= Tensor("foldl_1/while/Identity_1:0", shape=(), dtype=int32)
b= Tensor("foldl_1/while/TensorArrayReadV3:0", shape=(), dtype=int32)
2018-09-20 11:18:03.284305: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2018-09-20 11:18:03.284521: I tensorflow/core/common_runtime/process_util.cc:69] Creating new thread pool with default inter op setting: 4. Tune using inter_op_parallelism_threads for best performance.
method one
elems =  [1 2 3 4 5 6]
initializer=0 sum1 result= 21
initializer=10 sum2 result= 31
initializer=0 sum3 result= 21
"""