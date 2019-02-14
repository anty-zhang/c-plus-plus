# -*- coding: utf-8 -*-
from parallel_process.comm import *

# ######### OBSCURE TF CONTROL FLOW (Randomize JIT) ##########
reset()

# input whole dataset
input_ph_nx = tf.placeholder(tf.float32, shape=[None, X_nx.shape[1]])
output_ph_ny = tf.placeholder(tf.float32, shape=[None, Y_ny.shape[1]])
n = tf.shape(input_ph_nx)[0]

# generate random batches up front
# i = iterations

# generate variables for net
opt = tf.train.AdamOptimizer(1e-2)


def while_fn(t):
    batch_ix_b = tf.random_uniform([batch_size], 0, n, dtype=tf.int32)
    X_bx = tf.gather(input_ph_nx, batch_ix_b)
    Y_by = tf.gather(output_ph_ny, batch_ix_b)
    with tf.control_dependencies([t]):
        pred_by = mlp(X_bx)
        loss = tf.losses.mean_squared_error(Y_by, pred_by)
        with tf.control_dependencies([opt.minimize(loss)]):
            return t + 1


training = tf.while_loop(lambda t: t < nbatches,
                         while_fn, [0], back_prop=False)

pred_ny = mlp(input_ph_nx)
tot_loss = tf.losses.mean_squared_error(output_ph_ny, pred_ny)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    fd = {input_ph_nx: X_nx, output_ph_ny: Y_ny}
    loss_before = sess.run(tot_loss, feed_dict=fd)
    t = time.time()
    sess.run(training, feed_dict=fd)
    t = time.time() - t
    loss_after = sess.run(tot_loss, feed_dict=fd)

print('*' * 40)
print('while', t, 'sec')
print('loss', loss_before, '->', loss_after)
print('*' * 40)

"""
/Users/didi/anaconda3/envs/tf/bin/python /Users/didi/didi/work/tf_example/tf_random_speed_4.py
/Users/didi/anaconda3/envs/tf/lib/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88
  return f(*args, **kwds)
/Users/didi/anaconda3/envs/tf/lib/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88
  return f(*args, **kwds)
2018-09-20 11:43:37.698347: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2018-09-20 11:43:37.698592: I tensorflow/core/common_runtime/process_util.cc:69] Creating new thread pool with default inter op setting: 4. Tune using inter_op_parallelism_threads for best performance.
****************************************
while 39.98440194129944 sec
loss 4550.195 -> 4.8637033
****************************************
"""