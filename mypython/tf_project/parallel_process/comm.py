# -*- coding: utf-8 -*-

"""
reference: https://gist.githubusercontent.com/vlad17/5d67eef9fb06c6a679aeac6d07b4dc9c/raw/50aeded2eab0ff0c49ccf6f477fc70ae7283698a/tf_random_speed.py
https://vlad17.github.io/2017/12/23/beating-tf-api-in-vram.html
"""


# vladimir feinberg 23 dec 2017 tf 1.4
# feel free to use under Apache 2.0 License terms
import time

import numpy as np
import tensorflow as tf

# pretend we don't have X, Y available until we're about
# to train the network, so we have to use placeholders. This is the case
# in, e.g., RL.
np.random.seed(1234)
X_nx = np.random.uniform(size=(1000 * 1024, 64))
Y_ny = np.column_stack([X_nx.sum(axis=1),
                        np.log(X_nx).sum(axis=1),
                        np.exp(X_nx).sum(axis=1),
                        np.sin(X_nx).sum(axis=1)])
nbatches = 10000
batch_size = 512


def mlp(in_bx, ydim=Y_ny.shape[1], width=32, depth=5, scope='mlp'):
    with tf.variable_scope(scope, reuse=tf.AUTO_REUSE):
        out = in_bx
        for _ in range(depth):
            out = tf.layers.dense(out, width, activation=tf.nn.relu)
        out = tf.layers.dense(out, ydim)
    return out


def reset():
    tf.reset_default_graph()
    tf.set_random_seed(1234)
    np.random.seed(1234)