# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
import os
import shutil

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

LOG_DIR = "./logs"

if os.path.exists(LOG_DIR):
    shutil.rmtree(LOG_DIR)

########################################################################################################################
# 加载数据
digits = load_digits()
X = digits.data     # shape=(1797, 64)
Y = digits.target   # shape=(1797, 1)

y = LabelBinarizer().fit_transform(Y)           # shape=(1797, 10)
X_train, x_test, Y_train, y_test = train_test_split(X, y, test_size=.3)


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

        # here to dropout
        Wx_plus_b = tf.nn.dropout(Wx_plus_b, keep_prob=keep_prob)

        print("Wx_plus_b=", Wx_plus_b)

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)

    tf.summary.histogram(layer_name + '/outputs', outputs)

    return outputs


########################################################################################################################
# 搭建网络
with tf.name_scope('inputs'):
    keep_prob = tf.placeholder(tf.float32)
    xs = tf.placeholder(tf.float32, [None, 8*8], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 10], name='y_input')

# add output layer
l1 = add_layer(xs, 64, 50, n_layer=1, activation_function=tf.nn.relu)
prediction = add_layer(l1, 50, 10, n_layer=2, activation_function=tf.nn.softmax)

# loss
# error InvalidArgumentError (see above for traceback): Nan in summary histogram for: layer2/weight/layer2/weights
# cross_entropy = tf.reduce_mean(- tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
cross_entropy = tf.reduce_mean(- tf.reduce_sum(ys * tf.log(tf.clip_by_value(prediction, 1e-10, 1.0)), reduction_indices=[1]))
train = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

# loss summary
tf.summary.scalar("loss", cross_entropy)


########################################################################################################################
# 训练

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # summary writer goes here
    merged = tf.summary.merge_all()
    train_writer = tf.summary.FileWriter("logs/train", sess.graph)
    test_writer = tf.summary.FileWriter("logs/test", sess.graph)

    for step in range(10000):
        # sess.run(train, feed_dict={xs: X_train, ys: Y_train})
        sess.run(train, feed_dict={xs: X_train, ys: Y_train, keep_prob: 0.5})

        if step % 50 == 0:
            # record loss
            train_result = sess.run(merged, feed_dict={xs: X_train, ys: Y_train, keep_prob: 1.0})
            test_result = sess.run(merged, feed_dict={xs: x_test, ys: y_test, keep_prob: 1.0})

            train_writer.add_summary(train_result, step)
            test_writer.add_summary(test_result, step)
