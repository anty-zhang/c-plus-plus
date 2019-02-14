"""
https://github.com/MorvanZhou/tutorials/blob/master/tensorflowTUT/tf20_RNN2/full_code.py
https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/3_NeuralNetworks/recurrent_network.py
"""
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

# train data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


########################################################################################################################
# hyper parameters
training_iters = 100000
lr = 0.001
batch_size = 128
n_input = 28            # MNIST data input (image shape: 28*28)
n_steps = 28            # time steps
n_hidden_units = 128    # neurons in hidden layer
n_classes = 10          # MNIST data classes (0-9)

########################################################################################################################
# variant parameters
# tf Graph input
x = tf.placeholder(tf.float32, [None, n_steps, n_input], name="x")
y = tf.placeholder(tf.float32, [None, n_classes], name='y')

# define weights
weights = {
    # (n_input, n_hidden_units) = (28, 128)
    'in': tf.Variable(tf.random_normal([n_input, n_hidden_units])),
    # (n_hidden_units, n_classes) = (128, 10)
    'out': tf.Variable(tf.random_normal([n_hidden_units, n_classes]))
}

biases = {
    # (n_hidden_units, ) = (128, )
    'in': tf.Variable(tf.constant(0.1, shape=[n_hidden_units, ])),
    # (n_classes, ) = (10, )
    'out': tf.Variable(tf.constant(0.1, shape=[n_classes, ]))
}


########################################################################################################################
# define RNN
def RNN(X, weights_dict, biases_dict):
    ###############################################################################
    # hidden layer for input to cell
    # transpose the inputs shape from
    # 原始的 X 是 3 维数据, 我们需要把它变成 2 维数据才能使用 weights 的矩阵乘法
    # X ==> (128 batch, 28 steps, 28 inputs)
    X = tf.reshape(X, [-1, n_input])

    # into hidden
    # X_in = (128 batch * 28 steps, 128 hidden)
    # X_in = W * X + b
    X_in = tf.matmul(X, weights_dict['in']) + biases_dict['in']
    # X_in ==> (128 batch, 28 steps, 128 hidden)
    X_in = tf.reshape(X_in, [-1, n_steps, n_hidden_units])

    ###############################################################################
    # cell

    cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden_units, forget_bias=1.0, state_is_tuple=True)
    init_state = cell.zero_state(batch_size=batch_size, dtype=tf.float32)   # 初始化全零 state

    # You have 2 options for following step.
    # 1: tf.nn.rnn(cell, inputs);
    # 2: tf.nn.dynamic_rnn(cell, inputs).
    # 不推荐1原因：http://www.wildml.com/2016/08/rnns-in-tensorflow-a-practical-guide-and-undocumented-features/
    # If use option 1, you have to modified the shape of X_in, go and check out this:
    # https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/3_NeuralNetworks/recurrent_network.py
    # In here, we go for option 2.
    # dynamic_rnn receive Tensor (batch, steps, inputs) or (steps, batch, inputs) as X_in.
    # Make sure the time_major is changed accordingly.
    # 如果 inputs 为(batches, steps, inputs) == > time_major=False;
    # 如果 inputs 为 (steps, batches, inputs) ==> time_major=True
    # dynamic_rnn= tensorflow.python.ops.rnn
    # outputs=[batch, steps, hidden]
    outputs, final_state = tf.nn.dynamic_rnn(cell, X_in, initial_state=init_state, time_major=False)

    ###############################################################################
    # hidden layer for output as the final results
    # function 1
    # results = tf.matmul(final_state[1], weights['out']) + biases['out']

    # function 2
    # tf.transpose(outputs, [1, 0, 2]) ==> [steps, batch, hidden]
    # tf.unstack ==> [batch, hidden] = (128, 128)
    outputs = tf.unstack(tf.transpose(outputs, [1, 0, 2]))      # output为最后一个step的batch个输出
    # results ==> [batch, n_classes] = (128, 10)
    results = tf.matmul(outputs[-1], weights_dict['out']) + biases_dict['out']
    return results


########################################################################################################################
# train
pred = RNN(x, weights, biases)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
train_op = tf.train.AdamOptimizer(lr).minimize(cost)

correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

########################################################################################################################
# session
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    step = 0
    while step * batch_size < training_iters:
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs = batch_xs.reshape([batch_size, n_steps, n_input])
        sess.run([train_op], feed_dict={x: batch_xs, y: batch_ys})

        if step % 20 == 0:
            print(sess.run(accuracy, feed_dict={x:batch_xs, y: batch_ys}))

        step += 1
