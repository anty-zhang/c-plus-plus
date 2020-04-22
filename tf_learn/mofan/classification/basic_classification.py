# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

# 定义数据集的大小
DATASET_SIZE = 128
BATCH_SIZE = 8
STEP = 500

# 定义神经网络的参数
w1 = tf.Variable(tf.random_normal(shape=[2, 3], mean=0.0, stddev=1.0, seed=1))
w2 = tf.Variable(tf.random_normal(shape=[3, 1], mean=0.0, stddev=1.0, seed=1))

b1 = tf.Variable(tf.zeros([1, 3]) + 0.1)
b2 = tf.Variable(tf.zeros([1, 1]) + 0.1)

# 定义输入和输出
x = tf.placeholder(tf.float32, shape=(None, 2), name="x-input")
y_ = tf.placeholder(tf.float32, shape=(None, 1), name="y-input")

# 定义神经网络的前向传播过程
l1 = tf.matmul(x, w1) + b1
l2 = tf.matmul(l1, w2) + b2
y = tf.nn.sigmoid(l2)

cross_entropy = - tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0))
                                 + (1-y_) * tf.log(tf.clip_by_value(1-y, 1e-10, 1.0)))
train_step = tf.train.AdamOptimizer(0.01).minimize(cross_entropy)

# 通过随机函数生成一个模拟数据集
# 模拟输入是一个二维数组
X = np.random.RandomState(seed=1).rand(DATASET_SIZE, 2)
# 定义输出值，将x1+x2 < 1的输入数据定义为正样本
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]

# print("Y=", Y)

if __name__ == "__main__":
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)

        iter_num = int(X.shape[0] / BATCH_SIZE)

        for s in range(STEP):

            for i in range(iter_num):
                start_index = i * BATCH_SIZE
                end_index = (i + 1) * BATCH_SIZE

                sess.run([train_step], feed_dict={x: X[start_index: end_index], y_: Y[start_index: end_index]})

            if s % 50 == 0:
                # 计算所有数据的交叉熵
                total_cross_entropy = sess.run(cross_entropy, feed_dict={x: X, y_: Y})
                print("After %d training step(s), cross entropy on all data is %g" % (s, total_cross_entropy))

                pred_y = sess.run(y, feed_dict={x: X})

                # prediction_tensor = tf.convert_to_tensor(pred_y)
                # label_tensor = tf.convert_to_tensor(Y)

                auc_value, auc_op = tf.metrics.auc(Y, pred_y, num_thresholds=200)
                accuracy, update_op = tf.metrics.accuracy(Y, pred_y)
                # auc_value, auc_op = tf.metrics.auc(label_tensor, prediction_tensor, num_thresholds=200)
                sess.run(tf.local_variables_initializer())

                correct_acc = tf.equal(pred_y, Y)
                myacc = sess.run(tf.reduce_mean(tf.cast(correct_acc, tf.float32)))

                sess.run([auc_op, update_op])
                auc_res, accuracy_res = sess.run([auc_value, accuracy])
                # auc = roc_auc_score(ys_train, prob_to_label(train_predict))
                print("train auc= %s, accuracy=%s, myacc=%s" % (auc_res, accuracy_res, myacc))

        # # 预测输入X的类别
        # pred_y = sess.run(y, feed_dict={x: X})
        #
        # for pred, real in zip(pred_y, Y):
        #     print(pred, real)



