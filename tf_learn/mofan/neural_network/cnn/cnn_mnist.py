# -*- coding: utf-8 -*-

import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


########################################################################################################################
# define public basic
def compute_accuracy(sess, v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs, keep_prob: 1})
    correct_predict = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_predict, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys, keep_prob: 1})
    return result


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, filer_size):
    # tf.nn.conv2d函数是tensoflow里面的二维的卷积函数
    # stride [1, x_movement, y_movement, 1]
    # Must have strides[0]=strides[3] = 1
    return tf.nn.conv2d(x, filer_size, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(input):
    # 为了得到更多的图片信息，padding时我们选的是一次一步，也就是strides[1]=strides[2]=1，这样得到的图片尺寸没有变化，而我们希望压缩一下图
    # 片也就是参数能少一些从而减小系统的复杂度，因此我们采用pooling来稀疏化参数，也就是卷积神经网络中所谓的下采样层
    # stride [1, x_movement, y_movement, 1]
    # 池化的核函数大小为2x2，因此ksize=[1,2,2,1]
    # 步长为2，因此strides=[1,2,2,1]
    return tf.nn.max_pool(input, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


########################################################################################################################
# define placeholder for inputs to network
xs = tf.placeholder(tf.float32, [None, 28 * 28])
ys = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)
# 把xs的形状变成[-1,28,28,1]，-1代表先不考虑输入的图片例子多少这个维度，后面的1是channel的数量，因为我们输入的图片是黑白的，
# 因此channel是1，例如如果是RGB图像，那么channel就是3
x_image = tf.reshape(xs, [-1, 28, 28, 1])   # [n_samples, 28, 28, 1]    将每个sample转为width * height * depth


########################################################################################################################
# def the network
# conv1 layer
# 卷积核patch的大小是5x5，因为黑白图片channel是1所以输入是1，输出是32个featuremap
filter_conv1 = weight_variable([5, 5, 1, 32])   # patch 5x5, in size 1, out size 32
b_conv1 = bias_variable([32])
hidden_conv1 = tf.nn.relu(conv2d(x_image, filter_conv1) + b_conv1)   # output size: 28x28x32
hidden_pool1 = max_pool_2x2(hidden_conv1)                       # output size: 14x14x32

# conv2 layer
filter_conv2 = weight_variable([5, 5, 32, 64])  # patch 5x5, in size 32, out size 64
b_conv2 = bias_variable([64])
hidden_conv2 = tf.nn.relu(conv2d(hidden_pool1, filter_conv2) + b_conv2)   # output size: 14x14x64
hidden_pool2 = max_pool_2x2(hidden_conv2)                                 # output size: 7x7x64

# full1 layer
w_fc1 = weight_variable([7*7*64, 1024])
b_fc1 = bias_variable([1024])
# [n_samples, 7, 7, 64] -> [n_samples, 7x7x64]
hidden_pool2_flat = tf.reshape(hidden_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(hidden_pool2_flat, w_fc1) + b_fc1)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob=keep_prob)

# full2 layer
f_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, f_fc2) + b_fc2)

########################################################################################################################
# loss
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)


########################################################################################################################
# train
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.5})

        if step % 50:
            print(compute_accuracy(sess, mnist.test.images, mnist.test.labels))
