# -*- coding: utf-8 -*-

"""
tf.cond(pred, true_fn=None, false_fn=None)
    pred=True执行true_fn
    pred=False执行false_fn

"""

import tensorflow as tf


# tf.cond 与 tf.control_dependencies 的控制问题
# 无论在pred = Ture 还是 False，输出的结果都是2，都是pred = tf.constant(True)的情况
def wrong_case():
    pred = tf.constant(False)
    x = tf.Variable([1])
    assign_x_2 = tf.assign(x, [2])

    def update_x_2():
        print("update_x_2")
        with tf.control_dependencies([assign_x_2]):
            return tf.identity(x)

    y = tf.cond(pred, update_x_2, lambda: tf.identity(x))

    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        print(y.eval())


# If you want to perform a side effect (like an assignment) in one of the branches,
# you must create the op that performs the side effect inside the function that you pass to .
# Because execution in a TensorFlow graph flows forward through the graph, all operations that you refer to in
# either branch must execute before the conditional is evaluated. This means that both the true and the false
# branches receive a control dependency on the tf.assign() op
# 操作必须在函数中创建
def right_case():
    pred = tf.placeholder(tf.bool, shape=[])
    x = tf.Variable([1])

    # x_2 = tf.assign(x, [2])
    def update_x_2():
        print("update_x_2")
        assign_x_2 = tf.assign(x, [2])
        with tf.control_dependencies([assign_x_2]):
            return tf.identity(x)

    def update_x_3():
        return tf.assign(x, [3])

    # y = tf.cond(pred, update_x_2, lambda: tf.identity(x))
    y = tf.cond(pred, update_x_2, update_x_3)
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        print(y.eval(feed_dict={pred: False}))
        print(y.eval(feed_dict={pred: True}))


if __name__ == "__main__":
    wrong_case()
    print("="*20)
    right_case()

"""
    output:
        update_x_2
        [2]
        ====================
        update_x_2
        [3]
        [2]
"""