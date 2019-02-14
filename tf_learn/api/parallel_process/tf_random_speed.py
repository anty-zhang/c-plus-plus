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


########## NUMPY + FEED DICT ##########
reset()

input_ph_nx = tf.placeholder(tf.float32, shape=[None, X_nx.shape[1]])
output_ph_ny = tf.placeholder(tf.float32, shape=[None, Y_ny.shape[1]])
n = tf.shape(input_ph_nx)[0]

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

########## NUMPY + FEED DICT ##########
reset()

input_ph_nx = tf.placeholder(tf.float32, shape=[None, X_nx.shape[1]])
output_ph_ny = tf.placeholder(tf.float32, shape=[None, Y_ny.shape[1]])
n = tf.shape(input_ph_nx)[0]

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


########## OBSCURE TF CONTROL FLOW ##########
reset()

# input whole dataset
input_ph_nx = tf.placeholder(tf.float32, shape=[None, X_nx.shape[1]])
output_ph_ny = tf.placeholder(tf.float32, shape=[None, Y_ny.shape[1]])
n = tf.shape(input_ph_nx)[0]

# generate random batches up front
# i = iterations
batches_ib = tf.random_uniform((nbatches, batch_size), 0, n, dtype=tf.int32)

# generate variables for net
opt = tf.train.AdamOptimizer(1e-2)


def fold_fn(prev, batch_ix_b):
    X_bx = tf.gather(input_ph_nx, batch_ix_b)
    Y_by = tf.gather(output_ph_ny, batch_ix_b)
    with tf.control_dependencies([prev]):
        pred_by = mlp(X_bx)
        loss = tf.losses.mean_squared_error(Y_by, pred_by)
        with tf.control_dependencies([opt.minimize(loss)]):
            return tf.constant(0)


training = tf.foldl(fold_fn, batches_ib, 0, back_prop=False)

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
print('foldl', t, 'sec')
print('loss', loss_before, '->', loss_after)
print('*' * 40)

########## OBSCURE TF CONTROL FLOW (Randomize JIT) ##########
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

########## TENSORFLOW DATASET ##########
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