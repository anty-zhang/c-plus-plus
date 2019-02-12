# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np

x = np.asarray([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

x_p = tf.placeholder(tf.int32, [2, 2, 3])

y = tf.reduce_sum(x_p, axis=1)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    res = sess.run(y, feed_dict={x_p: x})
    print("x=", x)
    print("res=", res)
