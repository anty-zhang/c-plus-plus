# -*- coding: utf-8 -*-
# View more python learning tutorial on my Youtube and Youku channel!!!

# My tutorial website: https://morvanzhou.github.io/tutorials/

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("./MNIST_DATA", one_hot=False)

# Parameters
learning_rate = 0.01
training_epoch = 5
batch_size = 256
display_step = 1
examples_to_show = 10

# Network Parameters
n_input = 28 * 28       # MNIST data input(img shape: 28*28)

# tf Graph input(only pictures)
X = tf.placeholder(dtype=tf.float32, shape=[None, n_input], name='n_input')

# hidden layer settings
n_hidden_1 = 256    # 1st layer num features
n_hidden_2 = 128    # 2nd layer num features

"""
在压缩环节：我们要把这个Features不断压缩，经过第一个隐藏层压缩至256个 Features，再经过第二个隐藏层压缩至128个。
在解压环节：我们将128个Features还原至256个，再经过一步还原至784个。
在对比环节：比较原始数据与还原后的拥有 784 Features 的数据进行 cost 的对比，根据 cost 来提升我的 Autoencoder 的准确率，下图是两个隐藏层的
weights 和 biases 的定义：
"""
weights = {
    'encoder_h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'encoder_h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),

    'decoder_h1': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_1])),
    'decoder_h2': tf.Variable(tf.random_normal([n_hidden_1, n_input]))
}

biases = {
    'encoder_b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'encoder_b2': tf.Variable(tf.random_normal([n_hidden_2])),

    'decoder_b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'decoder_b2': tf.Variable(tf.random_normal([n_input]))
}


# Building the encoder
def encoder(x):
    # Encoder Hidden layer with sigmoid activation #1
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder_h1']), biases['encoder_b1']))

    # Encoder Hidden layer with sigmoid activation #1
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['encoder_h2']), biases['encoder_b2']))

    return layer_2


# Building the decoder
def decoder(x):
    # Decoder Hidden layer with sigmod activation #1
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['decoder_h1']), biases['decoder_b1']))
    # Decoder Hidden layer with sigmod activation #2
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['decoder_h2']), biases['decoder_b2']))

    return layer_2


# Construct model
encoder_op = encoder(X)
decoder_op = decoder(encoder_op)


# Prediction
y_pred = decoder_op
# Targets are the input data
y_true = X

# define loss and optimizer, minimize the squared error
# 再通过我们非监督学习进行对照，即对 “原始的有 784 Features 的数据集” 和 “通过 ‘Prediction’ 得出的有 784 Features 的数据集”
# 进行最小二乘法的计算，并且使 cost 最小化
cost = tf.reduce_mean(tf.pow(y_true - y_pred, 2))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

# Launch the graph
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

    total_batch = int(mnist.train.num_examples/batch_size)

    # Train cycle
    for epoch in range(training_epoch):
        # Loop over all batches
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # run optimization op(backprop) and cost op(to get loss value)
            _, c = sess.run([optimizer, cost], feed_dict={X: batch_xs})

        # Display logs per epoch step
        if epoch % display_step == 0:
            print("Epoch: ", "%04d" % (epoch + 1), "cost=", "{:.9f}".format(c))

    print("Optimization Finished!")

    # Applying encode and decode over test set
    encode_decode = sess.run(y_pred, feed_dict={X: mnist.test.images[:examples_to_show]})

    # Compare original images with their reconstructions
    f, a = plt.subplots(2, 10, figsize=(10, 2))
    for i in range(examples_to_show):
        a[0][i].imshow(np.reshape(mnist.test.images[i], (28, 28)))
        a[1][i].imshow(np.reshape(encode_decode[i], (28, 28)))

    plt.show()
