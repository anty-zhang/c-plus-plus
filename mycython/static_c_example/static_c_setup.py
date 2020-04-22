from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="static c compute",
    ext_modules=cythonize("static_c_compute.pyx")
)
