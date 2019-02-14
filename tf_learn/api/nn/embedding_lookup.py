# -*- coding: utf-8 -*-

"""
tf.nn.embedding_lookup(params,
    ids,
    partition_strategy='mod',
    name=None,
    validate_indices=True,
    max_norm=None)
=>选取一个张量中索引对应的元素

"""

import tensorflow as tf
import numpy as np

random_tensor = np.random.random([10, 1])
embedding_lookup = tf.nn.embedding_lookup(random_tensor, [2, 4])

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print("random_tensor=", random_tensor)
    print("embedding_lookup=")
    print(sess.run(embedding_lookup))


    """
    output:
        random_tensor= [[0.21300523]
         [0.53736371]
         [0.36708431]
         [0.66737693]
         [0.16399905]
         [0.56219167]
         [0.75784703]
         [0.17458462]
         [0.45191612]
         [0.91140126]]
        embedding_lookup=
        [[0.36708431]
         [0.16399905]]
    """
