from parallel_process.comm import *

# ######### NUMPY + FEED DICT ##########
reset()

input_ph_nx = tf.placeholder(tf.float32, shape=[None, X_nx.shape[1]])
output_ph_ny = tf.placeholder(tf.float32, shape=[None, Y_ny.shape[1]])
# n = tf.shape(input_ph_nx)[0]

# generate variables for net
opt = tf.train.AdamOptimizer(1e-2)
pred_ny = mlp(input_ph_nx)
tot_loss = tf.losses.mean_squared_error(output_ph_ny, pred_ny)
update = opt.minimize(tot_loss)

with tf.Session() as sess:
    fd = {input_ph_nx: X_nx, output_ph_ny: Y_ny}
    sess.run(tf.global_variables_initializer())
    loss_before = sess.run(tot_loss, feed_dict=fd)
    t = time.time()

    # 主要不同点，在for循环外面批量生成nbatches次的训练索引
    batches_ib = np.random.randint(X_nx.shape[0], size=(nbatches, batch_size))
    for batch_ix_b in batches_ib:
        sess.run(update, feed_dict={
            input_ph_nx: X_nx[batch_ix_b],
            output_ph_ny: Y_ny[batch_ix_b]})
    t = time.time() - t
    loss_after = sess.run(tot_loss, feed_dict=fd)

print('*' * 40)
print('feed_dict (randomize up-front)', t, 'sec')
print('loss', loss_before, '->', loss_after)
print('*' * 40)

"""
/Users/didi/anaconda3/envs/tf/bin/python /Users/didi/didi/work/tf_example/tf_random_speed_2.py
/Users/didi/anaconda3/envs/tf/lib/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88
  return f(*args, **kwds)
/Users/didi/anaconda3/envs/tf/lib/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88
  return f(*args, **kwds)
2018-09-19 22:08:08.674647: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2018-09-19 22:08:08.674840: I tensorflow/core/common_runtime/process_util.cc:69] Creating new thread pool with default inter op setting: 4. Tune using inter_op_parallelism_threads for best performance.
****************************************
feed_dict (randomize up-front) 44.883748054504395 sec
loss 4541.414 -> 3.9439418
****************************************
"""