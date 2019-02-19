# -*- coding: utf-8 -*-

"""
arithmetic operation
"""

import tensorflow as tf


x = tf.constant([1, 2, 3], dtype=tf.float32)

y = tf.constant([4, 5, 6], dtype=tf.float32)


with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

    print("tf.subtract(x, y)))=", sess.run(tf.subtract(x, y)))
    print("tf.subtract(x, 10)))=", sess.run(tf.subtract(x, 10)))
    print("tf.div(x, y)))=", sess.run(tf.div(x, y)))
    print("tf.div(x, 10)))=", sess.run(tf.div(x, 10)))
    print("tf.scalar_mul(2, x)))=", sess.run(tf.scalar_mul(2, x)))
    print("tf.multiply(x, y)))=", sess.run(tf.multiply(x, y)))
    print("tf.multiply(x, 3)))=", sess.run(tf.multiply(x, 3)))
    print("tf.add(x, 3)))=", sess.run(tf.add(x, 3)))
    print("tf.add(x, y)))=", sess.run(tf.add(x, y)))

    """
    output:
    tf.subtract(x, y)))= [-3. -3. -3.]
    tf.subtract(x, 10)))= [-9. -8. -7.]
    tf.div(x, y)))= [0.25 0.4  0.5 ]
    tf.div(x, 10)))= [0.1 0.2 0.3]
    tf.scalar_mul(2, x)))= [2. 4. 6.]
    tf.multiply(x, y)))= [ 4. 10. 18.]
    tf.multiply(x, 3)))= [3. 6. 9.]
    tf.add(x, 3)))= [4. 5. 6.]
    tf.add(x, y)))= [5. 7. 9.]
    """
