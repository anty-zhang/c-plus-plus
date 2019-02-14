# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


########################################################################################################################
# add_layer 功能
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_uniform([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

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
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])


########################################################################################################################
# 搭建网络
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
y_predict = add_layer(l1, 10, 1, activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(y_predict - ys), reduction_indices=[1]))
train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)


########################################################################################################################
# 可视化
# plot the real data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)   # 创建子图
ax.scatter(x_data, y_data)      # 散点图
plt.ion()   # 本次运行请注释，全局运行不要注释
plt.show()


########################################################################################################################
# 训练 并 可视化
#
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(1000):
        sess.run(train, feed_dict={xs: x_data, ys: y_data})

        # to see the step improvement
        if i % 50 == 0:
            # print(sess.run(loss, feed_dict={xs:x_data, ys:y_data}))
            predict_target = sess.run(y_predict, feed_dict={xs: x_data})

            try:
                ax.lines.remove(lines[0])
            except Exception as e:
                pass

            # plot the prediction
            lines = ax.plot(x_data, predict_target, 'r-', lw=5)
            plt.pause(0.1)
