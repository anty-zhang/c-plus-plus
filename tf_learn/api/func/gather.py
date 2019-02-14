import tensorflow as tf

r = tf.range(0, 10) * 10 + tf.constant(1, shape=[10])
r1 = tf.gather(r, [1, 3, 6, 9])

with tf.Session() as s:
    print(s.run(r))
    print(s.run(r1))

"""
result:
[ 1 11 21 31 41 51 61 71 81 91]
[11 31 61 91]

"""
