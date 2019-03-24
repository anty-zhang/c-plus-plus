# -*- coding: utf-8 -*-
"""
The basic idea about Nature Evolution Strategy with visualation.

Visit my tutorial website for more: https://morvanzhou.github.io/tutorials/
"""
import numpy as np
import tensorflow as tf
from tensorflow.contrib.distributions import MultivariateNormalFullCovariance
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


DNA_SIZE = 2        # parameter (solution) number
POP_SIZE = 100      # population size
N_GENERATION = 200  # training step
LR = 0.02           # learning rate


# fitness function
def get_fitness(pred):
    return -((pred[:, 0])**2 + pred[:, 1]**2)

# build multivariate distribution
mean = tf.Variable(tf.random_normal([2, ], 13., 1.), dtype=tf.float32)      # 均值
cov = tf.Variable(5. * tf.eye(DNA_SIZE), dtype=tf.float32)                  # 协方差
mvn = MultivariateNormalFullCovariance(loc=mean, covariance_matrix=cov)     # Construct Multivariate Normal distribution

make_kid = mvn.sample(POP_SIZE)     # sampling operation

# compute gradient and update mean and covariance matrix from sample and fitness

tf_kids_fitness = tf.placeholder(tf.float32, [POP_SIZE, ])
tf_kids = tf.placeholder(tf.float32, [POP_SIZE, DNA_SIZE])
loss = - tf.reduce_mean(mvn.log_prob(tf_kids) * tf_kids_fitness)    # log prob * fitness
train_op = tf.train.GradientDescentOptimizer(LR).minimize(loss)     # compute and apply gradients for mean and cov


# something about plotting (can be ignored)
n = 300
x = np.linspace(-20, 20, n)
X, Y = np.meshgrid(x, x)
Z = np.zeros_like(X)
for i in range(n):
    for j in range(n):
        Z[i, j] = get_fitness(np.array([[x[i], x[j]]]))
plt.contourf(X, Y, -Z, 100, cmap=plt.cm.rainbow)
plt.ylim(-20, 20)
plt.xlim(-20, 20)
plt.ion()


with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

    # training
    for g in range(N_GENERATION):
        kids = sess.run(make_kid)
        kids_fitness = get_fitness(kids)
        sess.run(train_op, feed_dict={tf_kids_fitness: kids_fitness, tf_kids: kids})    # update distribution parameters

        # plotting update
        if 'sca' in globals():
            sca.remove()

        sca = plt.scatter(kids[:, 0], kids[:, 1], s=30, c='k')
        plt.pause(0.05)

print('Finished')
plt.ioff()
plt.show()
