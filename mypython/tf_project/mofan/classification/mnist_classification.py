# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

########################################################################################################################
# MNIST 数据集
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_DATA', one_hot=True)


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
# 搭建网络
# 利用占位符定义我们所需的神经网络的输入。 tf.placeholder()就是代表占位符，这里的None
# 代表无论输入有多少都可以，因为输入只有一个特征，所以这里是1
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 28*28], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 10], name='y_input')

# add output layer
prediction = add_layer(xs, 784, 10, 1, activation_function=tf.nn.softmax)

# loss
cross_entropy = tf.reduce_mean(- tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
train = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)


########################################################################################################################
# 预测
def compute_accuracy(sess, v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})

    return result

########################################################################################################################
# 训练

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train, feed_dict={xs: batch_xs, ys: batch_ys})
        if step % 50 == 0:
            print(step, compute_accuracy(sess, mnist.test.images, mnist.test.labels))

