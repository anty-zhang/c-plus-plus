import tensorflow as tf


def scope1():
    with tf.variable_scope("a_variable_scope", reuse=tf.AUTO_REUSE):
        with tf.name_scope("a_name_scope"):
            initializer = tf.constant_initializer(value=10)
            v1 = tf.Variable([1], name="v1", dtype=tf.float32)
            v2 = tf.get_variable("v1", shape=[1, 2], dtype=tf.float32)

    print("v1: ", v1)
    print("v2: ", v2)
    print("------------------------------------------------------------------------")


def scope2():
    with tf.name_scope("b_variable_scope"):
        with tf.variable_scope("b_name_scope"):
            initializer = tf.constant_initializer(value=10)
            v1 = tf.Variable([1], name="v1", dtype=tf.float32)
            v2 = tf.get_variable("v1", shape=[1, 2], dtype=tf.float32)

    print("v1: ", v1)
    print("v2: ", v2)
    print("------------------------------------------------------------------------")

    """
    v1:  <tf.Variable 'a_variable_scope/a_name_scope/v1:0' shape=(1,) dtype=float32_ref>
    v2:  <tf.Variable 'a_variable_scope/v1:0' shape=(1, 2) dtype=float32_ref>
    ------------------------------------------------------------------------
    v1:  <tf.Variable 'b_variable_scope/b_name_scope/v1:0' shape=(1,) dtype=float32_ref>
    v2:  <tf.Variable 'b_name_scope/v1:0' shape=(1, 2) dtype=float32_ref>
    ------------------------------------------------------------------------
    """


def variable_not_reuse_test():
    # 设置GPU按需增长
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)

    # 拿官方的例子改动一下
    def my_image_filter():
        conv1_weights = tf.Variable(tf.random_normal([5, 5, 32, 32]), name="conv1_weights")
        conv1_biases = tf.Variable(tf.zeros([32]), name="conv1_biases")
        conv2_weights = tf.Variable(tf.random_normal([5, 5, 32, 32]), name="conv2_weights")
        conv2_biases = tf.Variable(tf.zeros([32]), name="conv2_biases")
        return None

    # First call creates one set of 4 variables.
    result1 = my_image_filter()
    # Another set of 4 variables is created in the second call.
    result2 = my_image_filter()
    # 获取所有的可训练变量
    all_varialbe = tf.trainable_variables()
    for v in all_varialbe:
        print(v)
    sess.close()
    print("------------------------------------------------------------------------")
    """
    <tf.Variable 'conv1_weights:0' shape=(5, 5, 32, 32) dtype=float32_ref>
    <tf.Variable 'conv1_biases:0' shape=(32,) dtype=float32_ref>
    <tf.Variable 'conv2_weights:0' shape=(5, 5, 32, 32) dtype=float32_ref>
    <tf.Variable 'conv2_biases:0' shape=(32,) dtype=float32_ref>
    <tf.Variable 'conv1_weights_1:0' shape=(5, 5, 32, 32) dtype=float32_ref>
    <tf.Variable 'conv1_biases_1:0' shape=(32,) dtype=float32_ref>
    <tf.Variable 'conv2_weights_1:0' shape=(5, 5, 32, 32) dtype=float32_ref>
    <tf.Variable 'conv2_biases_1:0' shape=(32,) dtype=float32_ref>
    ------------------------------------------------------------------------
    """


def variable_reuse_test():
    # 设置GPU按需增长
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)

    # 定义一个卷基层的通用方式
    def conv_relu(kernel_shape, bias_shape):
        # create variable name "weights"
        weights = tf.get_variable(name="weights", shape=kernel_shape, initializer=tf.random_normal_initializer())

        # create variable name "biases"
        biases = tf.get_variable(name="biases", shape=bias_shape, initializer=tf.constant_initializer(0.0))
        return 1

    def my_image_filter():
        # 定义卷基层
        # Variables created here will be named "conv1/weights", "conv1/biases".
        with tf.variable_scope("conv1"):
            relu1 = conv_relu([5, 5, 32, 32], [32])

        # # Variables created here will be named "conv2/weights", "conv2/biases".
        with tf.variable_scope("conv2"):
            relu2 = conv_relu([5, 5, 32, 32], [32])

        return relu1, relu2

    with tf.variable_scope("image_filters") as scope:
        # 下面我们两次调用 my_image_filter 函数，但是由于引入了 变量共享机制
        # 可以看到我们只是创建了一遍网络结构。
        result1 = my_image_filter()

        scope.reuse_variables()

        result2 = my_image_filter()

    for v in tf.trainable_variables():
        print(v)

    print("------------------------------------------------------------------------")
    sess.close()

    """
    <tf.Variable 'image_filters/conv1/weights:0' shape=(5, 5, 32, 32) dtype=float32_ref>
    <tf.Variable 'image_filters/conv1/biases:0' shape=(32,) dtype=float32_ref>
    <tf.Variable 'image_filters/conv2/weights:0' shape=(5, 5, 32, 32) dtype=float32_ref>
    <tf.Variable 'image_filters/conv2/biases:0' shape=(32,) dtype=float32_ref>
    """


def variable_reuse_test2():
    with tf.variable_scope("a_variable_scope") as scope:
        initializer = tf.constant_initializer(value=3)
        var3 = tf.get_variable(name='var3', shape=[1], dtype=tf.float32, initializer=initializer)
        scope.reuse_variables()
        var3_reuse = tf.get_variable(name='var3', )
        var4 = tf.Variable(name='var4', initial_value=[4], dtype=tf.float32)
        var4_reuse = tf.Variable(name='var4', initial_value=[4], dtype=tf.float32)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        print(var3.name)  # a_variable_scope/var3:0
        print(sess.run(var3))  # [ 3.]
        print(var3_reuse.name)  # a_variable_scope/var3:0
        print(sess.run(var3_reuse))  # [ 3.]
        print(var4.name)  # a_variable_scope/var4:0
        print(sess.run(var4))  # [ 4.]
        print(var4_reuse.name)  # a_variable_scope/var4_1:0
        print(sess.run(var4_reuse))  # [ 4.]


if __name__ == "__main__":
    # scope1()
    # scope2()
    # variable_not_reuse_test()
    # variable_reuse_test()

    variable_reuse_test2()
