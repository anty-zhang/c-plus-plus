# -*- coding: utf-8 -*-
"""
visit https://morvanzhou.github.io/tutorials/ for more!
Build two networks.
1. Without batch normalization
2. With batch normalization
Run tests on these two networks.
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# ACTIVATION = tf.nn.relu
ACTIVATION = tf.nn.tanh
N_LAYERS = 7
N_HIDDEN_UNITS = 30


def fix_seed(seed=27):
    np.random.seed(seed=seed)
    tf.set_random_seed(seed=seed)


def plot_his(inputs, inputs_norm):
    # plot histogram for the inputs of every layer
    for j, all_inputs in enumerate([inputs, inputs_norm]):
        for i, input in enumerate(all_inputs):
            plt.subplot(2, len(all_inputs), j * len(all_inputs) + (i + 1))
            plt.cla()
            if i == 0:
                the_range = (-7, 10)
            else:
                the_range = (-1, 1)
            plt.hist(input.ravel(), bins=15, range=the_range, color='#FF5733')
            plt.yticks(())
            if j == 1:
                plt.xticks(the_range)
            else:
                plt.xticks(())
            ax = plt.gca()
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
        plt.title("%s normalizing" % ("Without" if j == 0 else "With"))
    plt.draw()
    plt.pause(0.01)


def build_net(xs, ys, norm):
    def add_layer(inputs, in_size, out_size, activation_function=None, norm=False):
        # weights and biases (bad initialization for this case)
        weights = tf.Variable(tf.random_normal([in_size, out_size], mean=0., stddev=1.))
        biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)

        # fully connected product
        Wx_plus_b = tf.matmul(inputs, weights) + biases

        # normalization fully connected product
        if norm:
            # batch normalize
            # the dimension you wanna normalize, here [0] for batch
            # for image, you ranna do [0, 1, 2] for [batch, height, width] but not channel
            fc_mean, fc_var = tf.nn.moments(Wx_plus_b, axes=[0],)
            scale = tf.Variable(tf.ones([out_size]))
            shift = tf.Variable(tf.zeros([out_size]))
            epsion = 0.001

            # apply moving average for mean and var when train on batch
            ema = tf.train.ExponentialMovingAverage(decay=0.5)

            def mean_var_with_update():
                ema_apply_op = ema.apply([fc_mean, fc_var])
                with tf.control_dependencies([ema_apply_op]):
                    return tf.identity(fc_mean), tf.identity(fc_var)

            mean, var = mean_var_with_update()
            Wx_plus_b = tf.nn.batch_normalization(Wx_plus_b, mean, var, shift, scale, epsion)
            # simliar with this two steps:
            # Wx_plus_b = (Wx_plus_b - fc_mean)/ tf.sqrt(fc_var + 0.001)
            # Wx_plus_b = Wx_plus_b * scale + shift

        if activation_function:
            outputs = activation_function(Wx_plus_b)
        else:
            outputs = Wx_plus_b

        return outputs

    fix_seed(1)

    if norm:
        # NF for the first input
        # TODO when testing, you should fix fc_mean, fc_var instead of using tf.nn.moments
        fc_mean, fc_var = tf.nn.moments(xs, axes=[0])
        scale = tf.Variable(tf.ones([1]))
        shift = tf.Variable(tf.zeros([1]))
        epsilon = 0.001

        # apply moving average for mean and var when train on batch
        ema = tf.train.ExponentialMovingAverage(decay=0.5)

        def mean_var_with_update():
            ema_apply_op = ema.apply([fc_mean, fc_var])
            with tf.control_dependencies([ema_apply_op]):
                return tf.identity(fc_mean), tf.identity(fc_var)

        mean, var = mean_var_with_update()
        """
        mean, var = tf.cond(on_train,    # on_train 的值是 True/False
                    mean_var_with_update,   # 如果是 True, 更新 mean/var
                    lambda: (               # 如果是 False, 返回之前 fc_mean/fc_var 的Moving Average
                        ema.average(fc_mean),
                        ema.average(fc_var)
                        )
                    )
        """
        xs = tf.nn.batch_normalization(xs, mean, var, shift, scale, epsilon)

    # record inputs for every layer
    layer_inputs = [xs]

    # build hidden layers
    for l_n in range(N_LAYERS):
        layer_input = layer_inputs[l_n]
        in_size = layer_input.get_shape()[1].value

        output = add_layer(layer_input, in_size, N_HIDDEN_UNITS, ACTIVATION, norm)

        layer_inputs.append(output)     # add output for next run

    # build output layer
    prediction = add_layer(layer_inputs[-1], 30, 1, activation_function=None)
    cost = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
    train_op = tf.train.GradientDescentOptimizer(0.001).minimize(cost)
    return [train_op, cost, layer_inputs]


# make up data
fix_seed(1)
x_data = np.linspace(-7, 10, 2500)[:, np.newaxis]
np.random.shuffle(x_data)
noise = np.random.normal(0, 8, x_data.shape)
y_data = np.square(x_data) - 5 + noise

# plot input data
# plt.scatter(x_data, y_data)
# plt.show()

xs = tf.placeholder(tf.float32, [None, 1])      # [num_samples, num_features]
ys = tf.placeholder(tf.float32, [None, 1])

train_op, cost, layer_inputs = build_net(xs, ys, norm=False)                    # without BN
train_op_norm, cost_norm, layer_inputs_norm = build_net(xs, ys, norm=True)      # with BN

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

    # record cost
    cost_his = []
    cost_his_norm = []
    record_step = 5
    plt.ion()
    plt.figure(figsize=(7, 3))

    for i in range(250):
        if i % 50 == 0:
            # plot histogram
            all_inputs, all_inputs_norm = sess.run([layer_inputs, layer_inputs_norm], feed_dict={xs: x_data, ys: y_data})
            plot_his(all_inputs, all_inputs_norm)

        # train on batch
        sess.run([train_op, train_op_norm], feed_dict={xs: x_data[i*10:i*10+10], ys: y_data[i*10:i*10+10]})

        if i % record_step == 0:
            # record cost
            cost_his.append(sess.run(cost, feed_dict={xs: x_data, ys: y_data}))
            cost_his_norm.append(sess.run(cost_norm, feed_dict={xs: x_data, ys: y_data}))

    plt.ioff()
    plt.figure()
    plt.plot(np.arange(len(cost_his)) * record_step, np.array(cost_his), label='NO BN')
    plt.plot(np.arange(len(cost_his)) * record_step, np.array(cost_his_norm), label='BN')
    plt.legend()
    plt.show()
