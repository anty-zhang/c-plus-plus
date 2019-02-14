# tf.stack, tf.unstack

> stack 按axis方向堆叠, 例如axis=0, 按行进行堆叠; axis=1, 按列进行堆叠

> unstack 按axis方向拆成数组

```python
a = tf.constant([1,2,3])
b = tf.constant([4,5,6])

c = tf.stack([a,b], axis=0)
d = tf.stack([a,b], axis=1)

sess.run(c)
array([[1, 2, 3],
       [4, 5, 6]], dtype=int32)

sess.run(d)
array([[1, 4],
       [2, 5],
       [3, 6]], dtype=int32)
       
```

# name_scope and variable_scope

## 官方定义

> tf.name_scope create namespace for operators in the default graph (只给操作加前缀，更好管理操作命名空间)

> tf.variable_scope create namespace for both variables and operators in the default graph (给变量和操作同时加前缀)

> 和tf.get_variable配合使用，实现变量共享的功能

## 三种创建变量的方式

> tf.placeholder, tf.Variable, tf.get_variable

> 测试程序详见：tf_example/api/scope/three_create_variable_method.py

> 在tf.get_variable创建的变量之间会发生命名冲突

> 三种创建变量的方式用途分工明确：

> (1) tf.placeholder 占位符 trainable==False

> (2) tf.Variable 一般变量用这种方式定义。可选择trainable类型

> (3) tf.get_variable 一般和tf.variable_scope配合使用，实现变量共享功能。可选择 trainable类型

## name_scope, variable_scope

> tf.name_scope() 并不会对 tf.get_variable() 创建的变量有任何影响

> tf.name_scope() 主要是用来管理命名空间的，这样子让我们的整个模型更加有条理。而 tf.variable_scope() 的作用是为了实现变量共享，它和 tf.get_variable() 来完成变量共享的功能

> 测试程序： tf_example/api/scope/name_variable_scope.py



# tf.contrib.legacy_seq2seq.sequence_loss_by_example 详解



