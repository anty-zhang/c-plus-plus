# -*- coding: utf-8 -*-

"""
tf.control_dependencies()设计是用来控制计算流图的，给图中的某些计算指定顺序。即在执行op, tensor之前某些op,tensor首先被执行.

比如：我们想要获取参数更新后的值，那么我们可以这么组织我们的代码。
opt = tf.train.Optimizer().minize(loss)

with tf.control_dependencies([opt]):
  updated_weight = tf.identity(weight)

with tf.Session() as sess:
  tf.global_variables_initializer().run()
  sess.run(updated_weight, feed_dict={...}) # 这样每次得到的都是更新后的weight


with g.control_dependencies([a, b]):
  # Ops constructed here run after `a` and `b`.
  with g.control_dependencies([c, d]):
    # Ops constructed here run after `a`, `b`, `c`, and `d`.

# clear the control dependencies
with g.control_dependencies([a, b]):
  # Ops constructed here run after `a` and `b`.
  with g.control_dependencies(None):
    # Ops constructed here run normally, not waiting for either `a` or `b`.
    with g.control_dependencies([c, d]):
      # Ops constructed here run after `c` and `d`, also not waiting
      # for either `a` or `b`.

# attention
# WRONG
def my_func(pred, tensor):
  t = tf.matmul(tensor, tensor)
  with tf.control_dependencies([pred]):
    # The matmul op is created outside the context, so no control
    # dependency will be added.
    return t

# RIGHT
def my_func(pred, tensor):
  with tf.control_dependencies([pred]):
    # The matmul op is created in the context, so a control dependency
    # will be added.
    return tf.matmul(tensor, tensor)
"""

import tensorflow as tf


# not work case one
def case_one():
    w = tf.Variable(1.0)
    ema = tf.train.ExponentialMovingAverage(0.9)
    update = tf.assign_add(w, 1.0)

    ema_op = ema.apply([update])

    # 问题：sess.run([ema_val])， ema_op 都会被先执行，然后再计算ema_val，实际情况并不是这样，为什么？
    # 看源码会发现 ema.average(update) 不是一个 op，它只是从ema对象的一个字典中取出键对应的 tensor 而已然后赋值给ema_val
    # 这个 tensor是由一个在 tf.control_dependencies([ema_op]) 外部的一个 op 计算得来的，所以 control_dependencies会失效
    # 解决：ema_val = tf.identity(ema.average(update))
    with tf.control_dependencies([ema_op]):
        # ema_val = ema.average(update)
        ema_val = tf.identity(ema.average(update))

    with tf.Session() as sess:
        tf.global_variables_initializer().run()

        for i in range(3):
            print(sess.run([ema_val]))


# not work case two
def case_two():
    w = tf.Variable(1.0)
    ema = tf.train.ExponentialMovingAverage(0.9)
    update = tf.assign_add(w, 1.0)

    ema_op = ema.apply([update])

    # 问题：读取 w1 的值并不会触发 ema_op
    # 原因：在创建Varible时，tensorflow是移除了dependencies了的所以会出现 control 不住的情况
    # with ops.control_dependencies(None):
    # 解决：w1 = tf.identity(tf.Variable(2.0))
    with tf.control_dependencies([ema_op]):
        # w1 = tf.identity(tf.Variable(2.0))
        w1 = tf.Variable(2.0)
        ema_val = ema.average(update)

    with tf.Session() as sess:
        tf.global_variables_initializer().run()

        for i in range(3):
            print(sess.run([ema_val, w1]))


if __name__ == "__main__":
    case_one()
    print("="*20)
    case_two()

    """
        output:
        [0.20000005]
        [0.4800001]
        [0.8320002]
        ====================
        [0.0, 2.0]
        [0.0, 2.0]
        [0.0, 2.0]
    """
