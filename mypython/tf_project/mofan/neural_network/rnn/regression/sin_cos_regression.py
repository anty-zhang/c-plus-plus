"""
# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

RNN 来进行回归的训练 (Regression)
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


########################################################################################################################
# hyper parameters
BATCH_START = 0     # 建立 batch data 时候的 index
TIME_STEPS = 20     # back propagation through time 的 time_steps
BATCH_SIZE = 50
INPUT_SIZE = 1      # sin 数据输入 size
OUTPUT_SIZE = 1     # cos 数据输出 size
CELL_SIZE = 10      # RNN 的 hidden unit size
LR = 0.006          # learning rate


########################################################################################################################
# data
def get_batch():
    global BATCH_START, TIME_STEPS, BATCH_SIZE
    # xs shape = (50batch, 20 steps)
    xs = np.arange(BATCH_START, BATCH_START + BATCH_SIZE * TIME_STEPS).reshape(BATCH_SIZE, TIME_STEPS) / (10/np.pi)
    seq = np.sin(xs)
    res = np.cos(xs)

    BATCH_START += TIME_STEPS
    # plt.plot(xs[0, :], res[0, :], 'r', xs[0, :], seq[0, :], 'b--')
    #
    # plt.show()

    # print("xs: ", xs)
    # print("seq: ", seq)
    # return = [batch_size, steps, 1] = (50, 20, 1)
    # np.newaxis 把steps的行 变成列
    """
    例如：
        seq = [
            [1,2,3]
            [4,5,6]
            [7,8,9]
        ]
        seq.shape=(3,3)
        seq[:,:,np.newaxis] = [
            [[1],
             [2],
             [3]
            ],
            [[4],
             [5],
             [6]
            ],
            [[7],
             [8],
             [9]
            ]
        ]
        seq[:,:,np.newaxis].shape=(3,3,1)
    """
    return [seq[:, :, np.newaxis], res[:, :, np.newaxis], xs]


########################################################################################################################
# define LSTMRNN
class LSTMRNN(object):
    def __init__(self, n_steps, input_size, output_size, cell_size, batch_size):
        self.n_steps = n_steps              # time steps
        self.input_size = input_size
        self.output_size = output_size
        self.cell_size = cell_size          # hidden unit size
        self.batch_size = batch_size

        with tf.name_scope('inputs'):
            self.xs = tf.placeholder(tf.float32, [None, n_steps, input_size], name='xs')    # shape=(50, 20, 1)
            self.ys = tf.placeholder(tf.float32, [None, n_steps, output_size], name='ys')   # shape=(50, 20, 1)

        with tf.variable_scope('in_hidden'):
            self.add_input_layer()

        with tf.variable_scope('LSTM_cell'):
            self.add_cell()

        with tf.variable_scope('out_hidden'):
            self.add_output_layer()

        with tf.name_scope('cost'):
            self.compute_cost()

        with tf.name_scope('train'):
            self.train_op = tf.train.AdamOptimizer(LR).minimize(self.cost)

    def add_input_layer(self):
        l_in_x = tf.reshape(self.xs, [-1, self.input_size], name='3D_to_2D')   # (batch*n_step, input_size)
        # Ws=(input_size, cell_size)
        Ws_in = self._weight_variable([self.input_size, self.cell_size])
        # bs=(cell_size, )
        bs_in = self._bias_variable([self.cell_size, ])
        # l_in_y = (batch*n_step, cell_size)
        with tf.name_scope("Wx_plus_bias"):
            l_in_y = tf.matmul(l_in_x, Ws_in) + bs_in
        # reshape l_in_y ==> (batch, n_steps, cell_size)
        self.l_in_y = tf.reshape(l_in_y, [-1, self.n_steps, self.cell_size], name="2D_to_3D")

    def add_cell(self):
        lstm_cell = tf.contrib.rnn.BasicLSTMCell(self.cell_size, forget_bias=1.0, stagte_is_tuple=True)
        with tf.name_scope('initial_state'):
            self.cell_init_state = lstm_cell.zero_state(self.batch_size, dtype=tf.float32)

        self.cell_outputs, self.cell_final_state = tf.nn.dynamic_rnn(lstm_cell, self.l_in_y, initial_state=self.cell_init_state, time_major=False)

    def add_output_layer(self):
        # l_out_x = (batch * n_steps, cell_size)
        l_out_x = tf.reshape(self.cell_outputs, [-1, self.cell_size], name="3D_to_2D")
        Ws_out = self._weight_variable([self.cell_size, self.output_size])
        bs_out = self._bias_variable([self.output_size, ])
        # pred=(batch* n_steps, output_size)
        with tf.name_scope("Wx_plus_bias"):
            self.pred = tf.matmul(l_out_x, Ws_out) + bs_out

    def compute_cost(self):
        losses = tf.contrib.legacy_seq2seq.sequence_loss_by_example()

    @staticmethod
    def _weight_variable(shape, name="weights"):
        initializer = tf.random_normal_initializer(mean=0., stddev=1., dtype=tf.float32)
        return tf.get_variable(shape=shape, initializer=initializer, name=name)

    @staticmethod
    def _bias_variable(shape, name="bias"):
        initializer = tf.constant_initializer(0.1, dtype=tf.float32)
        return tf.get_variable(name=name, shape=shape, initializer=initializer)

    @staticmethod
    def ms_error(lables, logits):
        return tf.square(tf.subtract(lables, logits))


########################################################################################################################
#


########################################################################################################################
#


########################################################################################################################
#


########################################################################################################################
#


########################################################################################################################
#

if __name__ == "__main__":
    get_batch()
