# -*- coding: utf-8 -*-

"""
A tensor is a generalization of vectors and matrices to potentially higher dimensions
tensor可以是Variable，Constant，Placeholder等等。但是，官网上还有一句话值得注意：Unlike tf.Tensor objects,
a tf.Variable exists outside the context of a single session.run call.这个说明了variable的特殊性，这也就是
y = x 失效，而 y = tf.identity(x)有效的原因。同时，对于tf.control_dependencies，官网上有这么句话：control_inputs:
 A list of Operation or Tensor objects which must be executed or computed before running the operations
 defined in the context

"""

import tensorflow as tf


def wrong_case():
    x = tf.Variable(0.0)
    print("x=", x)
    x_plus_1 = tf.assign_add(x, 1)

    with tf.control_dependencies([x_plus_1]):
        y = x
        print("y=", y)

    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)

        for i in range(5):
            print(sess.run(y))


def right_case_1():
    x = tf.Variable(0.0)
    print("x=", x)
    x_plus_1 = tf.assign_add(x, 1)

    with tf.control_dependencies([x_plus_1]):
        # tf.identity属于tensorflow中的一个ops，跟x = x + 0.0
        # 的性质一样，返回一个tensor，受到tf.control_dependencies的约束，所以生效
        y = x + 0.0
        print("y=", y)

    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)

        for i in range(5):
            print(sess.run(y))


def right_case_2():
    x = tf.Variable(0.0)
    print("x=", x)
    x_plus_1 = tf.assign_add(x, 1)

    with tf.control_dependencies([x_plus_1]):
        y = tf.identity(x, name='x')
        print("y=", y)

    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)

        for i in range(5):
            print(sess.run(y))


if __name__ == "__main__":
    wrong_case()
    print("="*20)
    right_case_1()
    print("=" * 20)
    right_case_2()

    """
    output:
        x= <tf.Variable 'Variable:0' shape=() dtype=float32_ref>
        y= <tf.Variable 'Variable:0' shape=() dtype=float32_ref>
        0.0
        0.0
        0.0
        0.0
        0.0
        ====================
        x= <tf.Variable 'Variable_1:0' shape=() dtype=float32_ref>
        y= Tensor("add:0", shape=(), dtype=float32)
        1.0
        2.0
        3.0
        4.0
        5.0
        ====================
        x= <tf.Variable 'Variable_2:0' shape=() dtype=float32_ref>
        y= Tensor("x:0", shape=(), dtype=float32)
        1.0
        2.0
        3.0
        4.0
        5.0
    """
