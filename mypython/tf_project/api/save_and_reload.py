"""
saveing and restoring
https://blog.csdn.net/jk981811667/article/details/78904914
"""
import tensorflow as tf
import numpy as np


def save_mode():
    # Save to file
    # remember to define the same dtype and shape when restore
    W = tf.Variable([[1, 2, 3], [10, 20, 30]], dtype=tf.float32, name="weight")
    b = tf.Variable([[4, 5, 60]], dtype=tf.float32, name="b")

    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        # sess.run(W)
        # sess.run(b)
        # saver = tf.train.Saver()
        # saver = tf.train.Saver({"weight": W, "b": b})
        # saver = tf.train.Saver([W, b])
        saver = tf.train.Saver({v.op.name for v in [W, b]})
        save_path = saver.save(sess, "my_model/train_net.ckpt")
        print("save_path: ", save_path)


def reload_mode():
    # restore variables
    # redefine the same shape and same type for your variables

    W = tf.Variable(np.arange(6).reshape((2, 3)), dtype=tf.float32, name="weight")
    b = tf.Variable(np.arange(3).reshape((1, 3)), dtype=tf.float32, name="b")

    with tf.Session() as sess:
        # not need init step
        saver = tf.train.Saver()
        saver.restore(sess, "my_model/train_net.ckpt")
        print("weight: ", sess.run(W))
        print("b: ", sess.run(b))


if __name__ == "__main__":
    # save_mode()
    # time.sleep(1)
    reload_mode()

