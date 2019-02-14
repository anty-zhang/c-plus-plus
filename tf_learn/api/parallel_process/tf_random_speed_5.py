# -*- coding: utf-8 -*-
from parallel_process.comm import *

# ######### TENSORFLOW DATASET ##########
for bufsize in [1000, 10000, 100000, 1000000]:
    reset()

    input_ph_nx = tf.placeholder(tf.float32, shape=[None, X_nx.shape[1]])
    output_ph_ny = tf.placeholder(tf.float32, shape=[None, Y_ny.shape[1]])

    # make training dataset
    ds = tf.data.Dataset.from_tensor_slices((input_ph_nx, output_ph_ny))
    ds = ds.repeat()
    ds = ds.shuffle(buffer_size=bufsize)
    ds = ds.batch(batch_size)
    ds = ds.prefetch(buffer_size=(batch_size * 5))
    it = ds.make_initializable_iterator()
    opt = tf.train.AdamOptimizer(1e-2)

    def while_fn(t):
        with tf.control_dependencies([t]):
            next_bx, next_by = it.get_next()
            pred_by = mlp(next_bx)
            loss = tf.losses.mean_squared_error(next_by, pred_by)
            update = opt.minimize(loss)
            with tf.control_dependencies([update]):
                return t + 1
    training = tf.while_loop(lambda t: t < nbatches,
                             while_fn, [0], back_prop=False)

    pred_ny = mlp(input_ph_nx)
    tot_loss = tf.losses.mean_squared_error(output_ph_ny, pred_ny)

    with tf.Session() as sess:
        fd = {input_ph_nx: X_nx, output_ph_ny: Y_ny}
        sess.run(tf.global_variables_initializer())
        loss_before = sess.run(tot_loss, feed_dict=fd)
        t = time.time()
        sess.run(it.initializer, feed_dict=fd)
        sess.run(training)
        t = time.time() - t
        loss_after = sess.run(tot_loss, feed_dict=fd)

    print('*' * 40)
    print('tf dataset (bufsize', bufsize, ')', t, 'sec')
    print('loss', loss_before, '->', loss_after)
    print('*' * 40)

"""
/Users/didi/anaconda3/envs/tf/bin/python /Users/didi/didi/work/tf_example/tf_random_speed_5.py
/Users/didi/anaconda3/envs/tf/lib/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88
  return f(*args, **kwds)
/Users/didi/anaconda3/envs/tf/lib/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88
  return f(*args, **kwds)
2018-09-20 11:47:19.521879: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2018-09-20 11:47:19.522060: I tensorflow/core/common_runtime/process_util.cc:69] Creating new thread pool with default inter op setting: 4. Tune using inter_op_parallelism_threads for best performance.
****************************************
tf dataset (bufsize 1000 ) 49.33634877204895 sec
loss 4543.273 -> 4.20317
****************************************
****************************************
tf dataset (bufsize 10000 ) 51.1103310585022 sec
loss 4543.273 -> 3.8448594
****************************************
****************************************
tf dataset (bufsize 100000 ) 54.35532903671265 sec
loss 4543.273 -> 3.9761822
****************************************
****************************************
tf dataset (bufsize 1000000 ) 61.29388904571533 sec
loss 4543.273 -> 3.9233804
****************************************
"""