# -*- coding: utf-8 -*

import tensorflow as tf
import numpy as np

########################################################################################################################
# 创建数据
x_data = np.random.rand(100).astype(dtype=np.float32)
y_data = x_data * 0.1 + 0.3

########################################################################################################################
# 搭建模型
weight = tf.Variable(tf.random_uniform([1], -0.1, 0.1, seed=27))
bias = tf.Variable(tf.zeros([1]))
y = weight * x_data + bias
# 计算误差
# loss = tf.reduce_sum(tf.square(y - y_data))   # reduce_mean not reduce_sum
loss = tf.reduce_mean(tf.square(y - y_data))

########################################################################################################################
# 传播误差
# 反向传递误差的工作就教给optimizer了, 我们使用的误差传递方法是梯度下降法: Gradient Descent 让后我们使用 optimizer 来进行参数的更新.
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

########################################################################################################################
# 训练
# 到目前为止, 我们只是建立了神经网络的结构, 还没有使用这个结构. 在使用这个结构之前, 我们必须先初始化所有之前定义的Variable
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(weight), sess.run(bias))
