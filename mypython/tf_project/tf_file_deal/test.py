

import tensorflow as tf
import numpy as np


def main():
    filename_queue = tf.train.string_input_producer(["/Users/didi/didi/work/route-go/data/18/part-00000.csv",
                                                     "/Users/didi/didi/work/route-go/data/18/part-00001.csv"], num_epochs=1)
    reader = tf.TextLineReader()
    key, value = reader.read(filename_queue)

    _, value = reader.read(filename_queue)
    record_defaults = [["0"], ["0"], ["0"], ["0"], ["0"]]

    features = tf.decode_csv(value,
                             record_defaults=record_defaults,
                             field_delim=' ')
    # # features = [order_id, restore_routes, start_coord, end_coord, real_route]
    batch_lines = tf.train.shuffle_batch([features], seed=127, batch_size=2, capacity=20, min_after_dequeue=6,
                                         num_threads=1)


    i = 0
    with tf.Session() as sess:
        sess.run(tf.local_variables_initializer())
        # tf.train.start_queue_runners()
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord, sess=sess)

        num_examples = 0
        try:
            while True:

                res = sess.run([batch_lines])
                # print( res)
                num_examples += 1
        except tf.errors.OutOfRangeError:
            print ("There are", num_examples, "examples")

        coord.request_stop()
        coord.join(threads)

if __name__ == "__main__":
    main()

