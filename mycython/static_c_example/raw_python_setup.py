from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="raw python compute",
    ext_modules=cythonize("raw_python_compute.pyx")
)
