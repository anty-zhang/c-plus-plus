# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import shutil
import os


########################################################################################################################
# add_layer 功能
def add_layer(inputs, in_size, out_size, activation_function=None):
    with tf.name_scope('layer'):
        with tf.name_scope('weight'):
            Weights = tf.Variable(tf.random_uniform([in_size, out_size]), name='W')

        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')

        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases

        print("Wx_plus_b=", Wx_plus_b)

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)

    return outputs


########################################################################################################################
# 导入数据
x_data = np.linspace(-1, 1, 100, dtype=np.float32)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise

# 利用占位符定义我们所需的神经网络的输入。 tf.placeholder()就是代表占位符，这里的None
# 代表无论输入有多少都可以，因为输入只有一个特征，所以这里是1
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')


########################################################################################################################
# 搭建网络
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
y_predict = add_layer(l1, 10, 1, activation_function=None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(y_predict - ys), reduction_indices=[1]))

with tf.name_scope('train'):
    train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)


########################################################################################################################
# 训练 并 可视化
#

with tf.Session() as sess:
    LOG_DIR = "./log"

    if os.path.exists(LOG_DIR):
        shutil.rmtree(LOG_DIR)

    tf.summary.FileWriter(LOG_DIR, sess.graph)
