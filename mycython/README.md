
[TOC]

# 介绍
cython 是 python的C/C++扩展库，python自动生成C++代码然后再由C++生成C++的扩展模块库，然后python就可以跑C++代码了。


## example
### first example

```bash
# hello.pyx -> 用pyx 转为c++代码
# 
def day_hello():
    print("Hello World.")

# setup.py -> 通过cythonize来把它变成c++的代码
from distutils.core import setup
from Cython.Build import cythonize
setup(name = 'Hello world app', ext_modules = cythonize("hello.pyx"))

# 编译
python setup.py build

# 加载到python的site-packages库中
python setup.py install
```

## 通过静态类提高性能 --> static_compute.pyx

- cdef:

- cpdef:

## 调用C函数提供性能 --> static_c_compute.pyx

## 总结

- 浮点数计算，cython调用C/C++可以极大提高性能

- I/O 密集型调用C/C++函数不能提高性能，而多线程可以极大提高性能
