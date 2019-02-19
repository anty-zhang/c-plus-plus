# -*- coding: utf-8 -*-
# View more python learning tutorial on my Youtube and Youku channel!!!

# My tutorial website: https://morvanzhou.github.io/tutorials/

import tensorflow as tf
import matplotlib.pyplot as plt

# Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./MNIST_DATA", one_hot=False)

# Parameters
learning_rate = 0.001
training_epoch = 20
batch_size = 256
display_step = 1

# Network Parameters
n_input = 28 * 28       # MNIST data input(img shape: 28*28)

# tf Graph input(only pictures)
X = tf.placeholder(dtype=tf.float32, shape=[None, n_input], name='n_input')

# hidden layer settings
n_hidden_1 = 128    # 1st layer num features
n_hidden_2 = 64     # 2nd layer num features
n_hidden_3 = 10     # 3nd layer num features
n_hidden_4 = 2      # 4nd layer num features

weights = {
    'encoder_h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'encoder_h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'encoder_h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_3])),
    'encoder_h4': tf.Variable(tf.random_normal([n_hidden_3, n_hidden_4])),

    'decoder_h1': tf.Variable(tf.random_normal([n_hidden_4, n_hidden_3])),
    'decoder_h2': tf.Variable(tf.random_normal([n_hidden_3, n_hidden_2])),
    'decoder_h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_1])),
    'decoder_h4': tf.Variable(tf.random_normal([n_hidden_1, n_input]))
}

biases = {
    'encoder_b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'encoder_b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'encoder_b3': tf.Variable(tf.random_normal([n_hidden_3])),
    'encoder_b4': tf.Variable(tf.random_normal([n_hidden_4])),

    'decoder_b1': tf.Variable(tf.random_normal([n_hidden_3])),
    'decoder_b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'decoder_b3': tf.Variable(tf.random_normal([n_hidden_1])),
    'decoder_b4': tf.Variable(tf.random_normal([n_input]))
}


# Building the encoder
def encoder(x):
    # Encoder Hidden layer with sigmoid activation #1
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder_h1']), biases['encoder_b1']))

    # Encoder Hidden layer with sigmoid activation #2
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['encoder_h2']), biases['encoder_b2']))

    # Encoder Hidden layer with sigmoid activation #3
    layer_3 = tf.nn.sigmoid(tf.add(tf.matmul(layer_2, weights['encoder_h3']), biases['encoder_b3']))

    # Encoder Hidden layer with sigmoid activation #4
    # 在第四层时，输出量不再是 [0,1] 范围内的数，而是将数据通过默认的 Linear activation function 调整为 (-∞,∞)
    layer_4 = tf.add(tf.matmul(layer_3, weights['encoder_h4']), biases['encoder_b4'])

    return layer_4


# Building the decoder
def decoder(x):
    # Decoder Hidden layer with sigmod activation #1
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['decoder_h1']), biases['decoder_b1']))
    # Decoder Hidden layer with sigmod activation #2
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['decoder_h2']), biases['decoder_b2']))
    # Decoder Hidden layer with sigmod activation #3
    layer_3 = tf.nn.sigmoid(tf.add(tf.matmul(layer_2, weights['decoder_h3']), biases['decoder_b3']))
    # Decoder Hidden layer with sigmod activation #4
    layer_4 = tf.nn.sigmoid(tf.add(tf.matmul(layer_3, weights['decoder_h4']), biases['decoder_b4']))
    return layer_4


# Construct model
encoder_op = encoder(X)
decoder_op = decoder(encoder_op)


# Prediction
y_pred = decoder_op
# Targets are the input data
y_true = X

# define loss and optimizer, minimize the squared error
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
    encode_result = sess.run(encoder_op, feed_dict={X: mnist.test.images})
    plt.scatter(encode_result[:, 0], encode_result[:, 1], c=mnist.test.labels)
    plt.colorbar()
    plt.show()
