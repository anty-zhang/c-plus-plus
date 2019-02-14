# -*- coding: utf-8 -*

import tensorflow as tf
import numpy as np

state = tf.Variable(0, name="counter")

# 定义变量one
one = tf.constant(1)

# 定义加法
new_value = tf.add(state, one)

# 将state更新为新的new
update = tf.assign(state, new_value)

# 初始化变量
init = tf.global_variables_initializer()


with tf.Session() as sess:
    sess.run(init)

    for _ in range(4):
        sess.run(update)
        print(sess.run(state))

