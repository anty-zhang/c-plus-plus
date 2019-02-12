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
# nbatches = 1
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


########## NUMPY + FEED DICT ##########
reset()

input_ph_nx = tf.placeholder(tf.float32, shape=[None, X_nx.shape[1]])   # (?, 64)
output_ph_ny = tf.placeholder(tf.float32, shape=[None, Y_ny.shape[1]])  # (?, 4)
# n = tf.shape(input_ph_nx)[0]    # n = 1000 * 1024

opt = tf.train.AdamOptimizer(1e-2)
pred_ny = mlp(input_ph_nx)
tot_loss = tf.losses.mean_squared_error(output_ph_ny, pred_ny)
update = opt.minimize(tot_loss)

with tf.Session() as sess:
    fd = {input_ph_nx: X_nx, output_ph_ny: Y_ny}
    sess.run(tf.global_variables_initializer())
    loss_before = sess.run(tot_loss, feed_dict=fd)
    t = time.time()
    for _ in range(nbatches):
        # 主要不同点，在for循环内面批量生成batch_size训练索引
        batch_ix_b = np.random.randint(X_nx.shape[0], size=(batch_size,))
        sess.run(update, feed_dict={
            input_ph_nx: X_nx[batch_ix_b],
            output_ph_ny: Y_ny[batch_ix_b]})
    t = time.time() - t
    loss_after = sess.run(tot_loss, feed_dict=fd)

print('*' * 40)
print('feed_dict (randomize jit)', t, 'sec')
print('loss', loss_before, '->', loss_after)
print('*' * 40)

"""
/Users/didi/anaconda3/envs/tf/bin/python /Users/didi/didi/work/tf_example/tf_random_speed_1.py
/Users/didi/anaconda3/envs/tf/lib/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88
  return f(*args, **kwds)
/Users/didi/anaconda3/envs/tf/lib/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88
  return f(*args, **kwds)
2018-09-19 21:54:18.920726: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2018-09-19 21:54:18.921014: I tensorflow/core/common_runtime/process_util.cc:69] Creating new thread pool with default inter op setting: 4. Tune using inter_op_parallelism_threads for best performance.
****************************************
feed_dict (randomize jit) 47.759294271469116 sec
loss 4541.414 -> 3.9439418
****************************************
"""
