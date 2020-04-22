from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="static func and var compute",
    ext_modules=cythonize("static_compute.pyx")
)
