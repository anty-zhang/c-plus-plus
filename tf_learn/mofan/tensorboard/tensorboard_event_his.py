# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import shutil
import os

"""
exercise:
tf.summary.histogram
tf.summary.scalar
"""


########################################################################################################################
# add_layer 功能
def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    layer_name = 'layer%s' % n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope('weight'):
            Weights = tf.Variable(tf.random_uniform([in_size, out_size]), name='W')
            tf.summary.histogram(layer_name + '/weights', Weights)

        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
            tf.summary.histogram(layer_name + '/biases', biases)

        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases

        print("Wx_plus_b=", Wx_plus_b)

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)

    tf.summary.histogram(layer_name + '/outputs', outputs)

    return outputs


########################################################################################################################
# 导入数据
x_data = np.linspace(-1, 1, 300, dtype=np.float32)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise

# 利用占位符定义我们所需的神经网络的输入。 tf.placeholder()就是代表占位符，这里的None
# 代表无论输入有多少都可以，因为输入只有一个特征，所以这里是1
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')


########################################################################################################################
# 搭建网络
l1 = add_layer(xs, 1, 10, n_layer=1, activation_function=tf.nn.relu)
y_predict = add_layer(l1, 10, 1, n_layer=2, activation_function=None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(y_predict - ys), reduction_indices=[1]))

    # tf.summary.scalar for event
    tf.summary.scalar('loss', loss)

with tf.name_scope('train'):
    train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)


########################################################################################################################
# 训练 并 可视化
#


with tf.Session() as sess:
    LOG_DIR = "./log"

    sess.run(tf.global_variables_initializer())         # 必有

    if os.path.exists(LOG_DIR):
        shutil.rmtree(LOG_DIR)

    # merge all
    merged_summary = tf.summary.merge_all()
    writer = tf.summary.FileWriter(LOG_DIR, sess.graph)

    for i in range(100000):
        sess.run(train, feed_dict={xs: x_data, ys: y_data})

        if i % 20 == 0:
            rs = sess.run(merged_summary, feed_dict={xs: x_data, ys:y_data})
            writer.add_summary(rs, i)
            print("i=", i)
