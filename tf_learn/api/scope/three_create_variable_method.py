import tensorflow as tf

# 设置GPU按需增长
config = tf.ConfigProto()
config.gpu_options.allow_growth = True

sess = tf.Session(config=config)

########################################################################################################################
# first method of create variable
# placeholder

p_v1 = tf.placeholder(tf.float32, shape=[2, 3, 4])
p_v2 = tf.placeholder(tf.float32, shape=[2, 3, 4], name='p_v')
p_v3 = tf.placeholder(tf.float32, shape=[2, 3, 4], name='p_v')

print("p_v1.name: ", p_v1.name)
print("p_v2.name: ", p_v2.name)
print("p_v3.name: ", p_v3.name)
print("type(p_v3): ", type(p_v3))
print("p_v3: ", p_v3)
print("---------------------------------------------------------------------------------------------------------------")

"""
p_v1.name:  Placeholder:0
p_v2.name:  p_v:0
p_v3.name:  p_v_1:0
type(p_v3):  <class 'tensorflow.python.framework.ops.Tensor'>
p_v3:  Tensor("p_v_1:0", shape=(2, 3, 4), dtype=float32)
"""

########################################################################################################################
# second method of create variable
# tf.Variable

v_v1 = tf.Variable([1, 2], dtype=tf.float32)
v_v2 = tf.Variable([1, 2], dtype=tf.float32, name="V")
v_v3 = tf.Variable([1, 2], dtype=tf.float32, name="V")
print("v_v1.name: ", v_v1.name)
print("v_v2.name: ", v_v2.name)
print("v_v3.name: ", v_v3.name)
print("type(v_v3): ", type(v_v3))
print("v_v3: ", v_v3)

print("---------------------------------------------------------------------------------------------------------------")

"""
v_v1.name:  Variable:0
v_v2.name:  V:0
v_v3.name:  V_1:0
type(v_v3):  <class 'tensorflow.python.ops.variables.Variable'>
v_v3:  <tf.Variable 'V_1:0' shape=(2,) dtype=float32_ref>
"""

########################################################################################################################
# third method of create variable
# tf.get_variable

g_v1 = tf.get_variable(name="g_v1", shape=[])
# g_v2 = tf.get_variable(name="g_v1", shape=[2])
print("g_v1.name: ", g_v1.name)
print("type(g_v1): ", type(g_v1))
print("g_v1: ", g_v1)

print("---------------------------------------------------------------------------------------------------------------")

"""
g_v1.name:  g_v1:0
type(g_v1):  <class 'tensorflow.python.ops.variables.Variable'>
g_v1:  <tf.Variable 'g_v1:0' shape=() dtype=float32_ref>
"""

########################################################################################################################
# tf.trainable_variables能够将我们定义的所有的 trainable=True 的所有变量以一个list的形式返回
all_variable = tf.trainable_variables()
for v in all_variable:
    print(v)

"""
<tf.Variable 'Variable:0' shape=(2,) dtype=float32_ref>
<tf.Variable 'V:0' shape=(2,) dtype=float32_ref>
<tf.Variable 'V_1:0' shape=(2,) dtype=float32_ref>
<tf.Variable 'g_v1:0' shape=() dtype=float32_ref>
"""
