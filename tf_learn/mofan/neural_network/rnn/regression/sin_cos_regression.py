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
    # return shape [(50,20,1), (50,20,1),(50,20)]
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
        l_in_x = tf.reshape(self.xs, [-1, self.input_size], name='3D_to_2D')   # (batch*n_step, input_size)=(1000,1)
        # Ws=(input_size, cell_size)
        Ws_in = self._weight_variable([self.input_size, self.cell_size])    # shape=(input_size, cell_size)=(1, 10)
        # bs=(cell_size, )
        bs_in = self._bias_variable([self.cell_size, ])
        # l_in_y = (batch*n_step, cell_size)
        with tf.name_scope("Wx_plus_bias"):
            l_in_y = tf.matmul(l_in_x, Ws_in) + bs_in
        # reshape l_in_y ==> (batch, n_steps, cell_size)=(50, 20, 10)
        self.l_in_y = tf.reshape(l_in_y, [-1, self.n_steps, self.cell_size], name="2D_to_3D")

    def add_cell(self):
        lstm_cell = tf.contrib.rnn.BasicLSTMCell(self.cell_size, forget_bias=1.0, state_is_tuple=True)
        with tf.name_scope('initial_state'):
            self.cell_init_state = lstm_cell.zero_state(self.batch_size, dtype=tf.float32)

        self.cell_outputs, self.cell_final_state = tf.nn.dynamic_rnn(lstm_cell, self.l_in_y, initial_state=self.cell_init_state, time_major=False)

    def add_output_layer(self):
        # l_out_x = (batch * n_steps, cell_size)=(1000, 10)
        l_out_x = tf.reshape(self.cell_outputs, [-1, self.cell_size], name="3D_to_2D")
        Ws_out = self._weight_variable([self.cell_size, self.output_size])      # shape=(cell_size, output_size)=(10, 1)
        bs_out = self._bias_variable([self.output_size, ])
        # pred=(batch* n_steps, output_size)=(1000, 1)
        with tf.name_scope("Wx_plus_bias"):
            self.pred = tf.matmul(l_out_x, Ws_out) + bs_out

    def compute_cost(self):
        # TODO learn: tf.contrib.sequence_loss_by_example, tf.div
        losses = tf.contrib.legacy_seq2seq.sequence_loss_by_example(
            [tf.reshape(self.pred, [-1], name='reshape_pred')],
            [tf.reshape(self.ys, [-1], name='reshape_target')],
            [tf.ones([self.batch_size * self.n_steps], dtype=tf.float32)],
            average_across_timesteps=True,
            softmax_loss_function=self.ms_error,
            name='losses'
        )

        with tf.name_scope('average_cost'):
            self.cost = tf.div(
                tf.reduce_sum(losses, name='losses_sum'),
                self.batch_size,
                name='average_cost'
            )

            tf.summary.scalar('cost', self.cost)

    @staticmethod
    def _weight_variable(shape, name="weights"):
        initializer = tf.random_normal_initializer(mean=0., stddev=1., dtype=tf.float32)
        return tf.get_variable(shape=shape, initializer=initializer, name=name)

    @staticmethod
    def _bias_variable(shape, name="bias"):
        initializer = tf.constant_initializer(0.1, dtype=tf.float32)
        return tf.get_variable(name=name, shape=shape, initializer=initializer)

    @staticmethod
    def ms_error(labels, logits):
        return tf.square(tf.subtract(labels, logits))


if __name__ == "__main__":
    model = LSTMRNN(TIME_STEPS, INPUT_SIZE, OUTPUT_SIZE, CELL_SIZE, BATCH_SIZE)

    with tf.Session() as sess:
        merged = tf.summary.merge_all()
        writer = tf.summary.FileWriter("logs", sess.graph)

        init = tf.global_variables_initializer()
        sess.run(init)

        plt.ion()   # 连续模式, plot不会停止运行
        plt.show()

        for i in range(200):
            seq, res, xs = get_batch()
            if i == 0:
                feed_dict = {
                    model.xs: seq,
                    model.ys: res,
                }
            else:
                feed_dict = {
                    model.xs: seq,
                    model.ys: res,
                    model.cell_init_state: state
                }

            _, cost, state, pred = sess.run([model.train_op, model.cost, model.cell_final_state, model.pred],
                                            feed_dict=feed_dict)

            # plotting
            plt.plot(xs[0, :], res[0].flatten(), 'r', xs[0, :], pred.flatten()[:TIME_STEPS], 'b--')
            plt.ylim((-1.2, 1.2))
            plt.draw()
            plt.pause(0.3)

            if i % 20 == 0:
                print("cost:", round(cost, 4))
                result = sess.run(merged, feed_dict)
                writer.add_summary(result, i)
