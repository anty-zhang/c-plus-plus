# -*- coding: UTF-8 _*_
from __future__ import print_function
import datetime
from time import time
import os
import re
import sys
import numpy
import tensorflow as tf
from tensorflow.contrib import layers
import random


# Launch the graph
configure = tf.ConfigProto()
configure.gpu_options.allow_growth=True
# configure.gpu_options.per_process_gpu_memory_fraction = 0.45
configure.log_device_placement = False


model_id = sys.argv[0]
epochs = int(sys.argv[1])
train_days = int(sys.argv[2])
now_dir = "./"
model_dir = now_dir + "model_" + model_id + "/"
file_dir = "/nfs/private/rp/raw_origin_ftrl_sample2/"
weight_dir =  now_dir + "weight_file_"+ model_id + "/"

linear_id_map = {}

vacab_size = 1000000
batch_size = 256


class DataSet(object):
    def __init__(self, file_name):
        #self.instances = []
        self.batch_id = 0
        self.batchs_pos_link = []
        self.batchs_neg_link = []
        self.total_batch_size = 0
        self.nr_instance = 0
        self.X = []
        self.Y = []
        self.qid2negInstMap = {}
        self.qid2posInstMap = {}
        self.qid2InstMap = {}
        self.id2qid = []
        self.load_raw_attr_training_file(file_name)

    def load_raw_attr_training_file(self, file_name):
        for line in open(file_name):
            items = line.split(" ")
            orderid = items[0]
            sim = int(items[1])
            linkid_linkval = items[2:]
            feat2val = []
            self.id2qid.append(orderid)
            for l in linkid_linkval:
                linkid, linkval = l.strip().split(":")
                if linkid not in linear_id_map:
                    tmp_len = len(linear_id_map)
                    linear_id_map[linkid] = tmp_len
                feat2val.append([linear_id_map[linkid],float(linkval)])
            self.X.append(feat2val)
            self.Y.append(sim)
            if sim > 0:
                if orderid not in self.qid2posInstMap:
                    self.qid2posInstMap[orderid] = []
                self.qid2posInstMap[orderid].append(len(self.X) - 1)
            else:
                if orderid not in self.qid2negInstMap:
                    self.qid2negInstMap[orderid] = []
                self.qid2negInstMap[orderid].append(len(self.X) - 1)
            if orderid not in self.qid2InstMap:
                self.qid2InstMap[orderid] = []
            self.qid2InstMap[orderid].append(len(self.X) - 1)
        self.nr_instance = len(self.X)
    def shuffle(self):
        self.batch_id = 0
        pos_link = []
        neg_link = []

        inst_idx_vec = list(range(self.nr_instance))

        random.shuffle(inst_idx_vec)
        for i in inst_idx_vec:
            qid = self.id2qid[i]
            if self.Y[i] > 0 :
                pi = i
                if qid not in self.qid2negInstMap:
                    continue
                rdx = random.randint(0, len(self.qid2negInstMap[qid]) - 1)
                ni = self.qid2negInstMap[qid][rdx]
            else:
                if qid not in self.qid2posInstMap:
                    continue
                pi = self.qid2posInstMap[qid][0]
                ni = i
            pos_link.append(self.X[pi])
            neg_link.append(self.X[ni])


        itr = int(len(pos_link)/batch_size)
        last_batch_size = len(pos_link) % batch_size

        begin_itr_id = 0
        end_itr_id = batch_size

        for idx in range(0, itr):
            tmp_pos_link = pos_link[begin_itr_id:end_itr_id]
            tmp_neg_link = neg_link[begin_itr_id:end_itr_id]
            self.batchs_pos_link.append(tmp_pos_link)
            self.batchs_neg_link.append(tmp_neg_link)
            begin_itr_id += batch_size
            end_itr_id += batch_size
        # if last_batch_size != 0:
        #     tmp_pos_linkid = pos_linkid[begin_itr_id:end_itr_id]
        #     tmp_neg_linkid = pos_linkid[begin_itr_id:end_itr_id]
        self.total_batch_size = len(self.batchs_pos_link)


    def next(self):
        if self.batch_id == self.total_batch_size:
            self.batch_id = 0
        batch_id = self.batch_id

        batch_pos_linkid = [[linkid2val[0] for linkid2val in i] for i in self.batchs_pos_link[batch_id]]
        batch_pos_linkval = [[linkid2val[1] for linkid2val in i]for i in self.batchs_pos_link[batch_id]]
        batch_neg_linkid = [[linkid2val[0] for linkid2val in i] for i in self.batchs_neg_link[batch_id]]
        batch_neg_linkval = [[linkid2val[1] for linkid2val in i] for i in self.batchs_neg_link[batch_id]]

        batch_pos_linkid_len = [len(i) for i in self.batchs_pos_link[batch_id]]
        batch_neg_linkid_len = [len(i) for i in self.batchs_neg_link[batch_id]]
        max_pos_linkid_len = max(batch_pos_linkid_len)
        max_neg_linkid_len = max(batch_neg_linkid_len)

        for i in range(0,len(self.batchs_pos_link[batch_id])):
            instlen_pos = batch_pos_linkid_len[i]
            batch_pos_linkid[i] = batch_pos_linkid[i][0:instlen_pos] + [0] * (max_pos_linkid_len - instlen_pos)
            batch_pos_linkval[i] = batch_pos_linkval[i][0:instlen_pos] + [0] * (max_pos_linkid_len - instlen_pos)

            instlen_neg = batch_neg_linkid_len[i]
            batch_neg_linkid[i] = batch_neg_linkid[i][0:instlen_neg] + [0] * (max_neg_linkid_len - instlen_neg)
            batch_neg_linkval[i] = batch_neg_linkval[i][0:instlen_neg] + [0] * (max_neg_linkid_len - instlen_neg)

        self.batch_id += 1

        return batch_pos_linkid, batch_pos_linkval, batch_pos_linkid_len, batch_neg_linkid, batch_neg_linkval, batch_neg_linkid_len

    def has_next(self):
        return self.batch_id < self.total_batch_size

    def reset(self):
        self.batch_id = 0

    def clear(self):
        self.batch_id = 0
        self.batchs_pos_link = []
        self.batchs_neg_link = []
        self.total_batch_size = 0
        self.nr_instance = 0
        self.X = []
        self.Y = []
        self.qid2negInstMap = {}
        self.qid2posInstMap = {}
        self.qid2InstMap = {}
        self.id2qid = []


# tf Graph input
posLinkidFeat = tf.placeholder(tf.int32, [batch_size, None])
posLinkvalFeat = tf.placeholder(tf.float32, [batch_size, None])
posSeqlens = tf.placeholder(tf.int32, [batch_size])

negLinkidFeat = tf.placeholder(tf.int32, [batch_size, None])
negLinkvalFeat = tf.placeholder(tf.float32, [batch_size, None])
negSeqlens = tf.placeholder(tf.int32, [batch_size])

#lr_div = tf.placeholder("float")
dropout = tf.placeholder("float")
train_phase = tf.placeholder(tf.bool)

loss_sum = tf.Variable(0.0, name="loss_sum")
count = tf.Variable(0.0, name="count")
mean_loss = tf.div(loss_sum, count)
reset_op = tf.group(loss_sum.assign(0.0), count.assign(0))


def calTop1Sim100(qid2InstMap, weights):
    predictright = 0.0
    predictorder = 0.0
    for qid in qid2InstMap.values():
        mini = -1
        minpred = 100000000
        for t in qid:
            s = 0
            print(t)
            for linkid2fea in data_set.X[t]:
                s += weights[linkid2fea[0]] * linkid2fea[1]
            if s < minpred:
                mini = t
                minpred = s
            if data_set.Y[mini] == 1:
                predictright += 1.0
            predictorder += 1.0
    return predictright / predictorder


def FTRLRank(train_phase, dropout_prob):

    sm_pos_link = tf.sequence_mask(posSeqlens, tf.reduce_max(posSeqlens), tf.float32)
    sm_neg_link = tf.sequence_mask(negSeqlens, tf.reduce_max(negSeqlens), tf.float32)
    w_embeddings = tf.get_variable("w_embeddings", [vacab_size], initializer=tf.ones_initializer())
    #w_embeddings = tf.get_variable("w_embeddings", [vacab_size], initializer=tf.constant_initializer(10.0))
    #zero_mat = tf.fill([vacab_size], 0.01)
    #min_var = tf.Variable(tf.constant(0.01, shape=[vacab_size]))
    #w_embeddings = tf.where(tf.greater(w_embeddings, zero_mat), w_embeddings, min_var)
    w_embeddings = tf.clip_by_value(w_embeddings, 1e-6, 1e+3)
    w_pos_embedding = tf.nn.embedding_lookup(w_embeddings, posLinkidFeat)
    w_neg_embedding = tf.nn.embedding_lookup(w_embeddings, negLinkidFeat)

    res_pos = tf.multiply(tf.multiply(w_pos_embedding, posLinkvalFeat), sm_pos_link)
    res_neg = tf.multiply(tf.multiply(w_neg_embedding, negLinkvalFeat), sm_neg_link)

    pFi = tf.reduce_sum(res_pos, -1, keep_dims = True)
    nFi = tf.reduce_sum(res_neg, -1, keep_dims = True)

    Fi = nFi - pFi

    local_cost = -tf.log(tf.sigmoid(Fi))

    loss = tf.reduce_sum(local_cost)

    with tf.control_dependencies([local_cost]):
        update_op = tf.group(count.assign(tf.add(count, tf.cast(tf.size(local_cost), dtype=tf.float32))),
                             loss_sum.assign(tf.add(loss_sum, loss)))

    return local_cost, update_op, w_embeddings

with tf.name_scope("training"):
    cost, update_op_train, w_train = FTRLRank(train_phase, dropout)
    link_weights = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, "w_embeddings")
    link_gradients = tf.gradients(cost, link_weights)

    #link_gradients, global_norm = tf.clip_by_global_norm(tf.gradients(cost, link_weights), 5000)
    #link_optimizer = tf.train.MomentumOptimizer(learning_rate = 0.00001, momentum = 0.5)
    link_optimizer = tf.train.AdamOptimizer(learning_rate=0.000001)
    # link_optimizer = tf.train.FtrlOptimizer(learning_rate=0.01,
    #                                          initial_accumulator_value=0.1,
    #                                          l1_regularization_strength=0.001, l2_regularization_strength=0.0001)
    train_op = link_optimizer.apply_gradients(zip(link_gradients, link_weights))



tf.get_variable_scope().reuse_variables()
with tf.name_scope("validation"):
    cost, update_op_test, w_test = FTRLRank(train_phase, dropout)


def run_validation(weight_file, is_print):
    test_set = [DataSet(test_filename)]
    out = open(weight_file, "w")

    print(datetime.datetime.now(), "load test data finish\n")
    reset_op.run()
    for cur_test_set in test_set:
        cur_test_set.shuffle()
        while cur_test_set.has_next():
            batch_pos_linkid, batch_pos_linkval, batch_pos_linkid_len, batch_neg_linkid, batch_neg_linkval, batch_neg_linkid_len = cur_test_set.next()
            _, w_embeddings = sess.run([update_op_test, w_test], feed_dict={posLinkidFeat: batch_pos_linkid, posLinkvalFeat: batch_pos_linkval,
                                                posSeqlens: batch_pos_linkid_len,
                                                negLinkidFeat: batch_neg_linkid, negLinkvalFeat: batch_neg_linkval,
                                                negSeqlens: batch_neg_linkid_len,
                                                dropout: 0.0, train_phase: False})

        sim_value = calTop1Sim100(cur_test_set.qid2InstMap, w_embeddings)
        if is_print == True:
            PrintVector(w_embeddings, out)
        cur_test_set.clear()
    local_acc = mean_loss.eval()
    reset_op.run()
    out.close()
    return local_acc, sim_value

def PrintVector(B, out):
    id_linear_map = {v: k for k, v in linear_id_map.items()}
    for l in range(0, len(id_linear_map)):
        out.write(id_linear_map[l] + " " + str(B[l]) + "\n")

init = tf.global_variables_initializer()

train_set_path = [file_dir + "raw_origin_ftrl_sample2_07" + "{:0>2d}".format(i) for i in range(train_days, 0, -1) ]
test_filename = file_dir + "201807w3_test1_1_restore_testdata"
#weight_file = weight_dir

saver = tf.train.Saver(max_to_keep=0)
with tf.Session(config=configure) as sess:
    sess.run(init)
    for epoch in range(0, epochs):
        is_print = False
        start = time()
        reset_op.run()
        print("Epoch " + str(epoch))
        for d_train_path in train_set_path:
            print(d_train_path)
            if not os.path.isfile(d_train_path):
                continue
            data_set = DataSet(d_train_path)
            data_set.shuffle()
            while data_set.has_next():
                batch_pos_linkid, batch_pos_linkval, batch_pos_linkid_len, batch_neg_linkid, batch_neg_linkval, batch_neg_linkid_len = data_set.next()
                _, _, w_embeddings = sess.run([train_op, update_op_train, w_train],feed_dict = {posLinkidFeat:batch_pos_linkid, posLinkvalFeat:batch_pos_linkval, posSeqlens:batch_pos_linkid_len,
                                          negLinkidFeat:batch_neg_linkid, negLinkvalFeat:batch_neg_linkval, negSeqlens:batch_neg_linkid_len,
                                          dropout:0.0, train_phase:True })
            sim_value = calTop1Sim100(data_set.qid2InstMap, w_embeddings)
            print(sim_value)
            data_set.clear()
            #log_loss = mean_loss.eval()
            #print("CurEpoch " + " ".join([str(x) for x in [epoch, log_loss]]))

        train_log_loss = mean_loss.eval()
        isExists = os.path.exists(weight_dir)
        if not isExists:
            os.makedirs(weight_dir)
        weight_file = weight_dir + "model." + str(epoch)
        if epoch % 2 == 0:
            is_print = True
        test_log_loss, sim_value = run_validation(weight_file, is_print)
        elapsed = int(time() - start)
        print("Epoch " + " ".join([str(x) for x in [epoch, elapsed, train_log_loss, test_log_loss, sim_value]]))
        isExists = os.path.exists(model_dir)
        if not isExists:
            os.makedirs(model_dir)
        saver.save(sess, model_dir + "model_base.ckpt", global_step=epoch)