#!/usr/bin/env python
# coding=utf-8
import raw_python_compute
import static_compute
import static_c_compute

import time

lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826

start_time = time.clock()
raw_python_compute.f_compute(3.2, 6.9, 1000000)
end_time = time.clock()
print("runing1 time: %f s" % (end_time - start_time))
start_time = time.clock()
for i in range(1000000):
    raw_python_compute.spherical_distance(lon1, lat1, lon2, lat2)
end_time = time.clock()
print("runing2 time: %f s" % (end_time - start_time))

print("------------------------------------------------------------")

start_time = time.clock()
static_compute.f_compute(3.2, 6.9, 1000000)
end_time = time.clock()
print("runing1 time: %f s" % (end_time - start_time))
start_time = time.clock()
for i in range(1000000):
    static_compute.spherical_distance(lon1, lat1, lon2, lat2)
end_time = time.clock()
print("runing2 time: %f s" % (end_time - start_time))

print("------------------------------------------------------------")

start_time = time.clock()
static_c_compute.f_compute(3.2, 6.9, 1000000)
end_time = time.clock()
print("runing1 time: %f s" % (end_time - start_time))
start_time = time.clock()
for i in range(1000000):
    static_c_compute.spherical_distance(lon1, lat1, lon2, lat2)
end_time = time.clock()
print("runing2 time: %f s" % (end_time - start_time))

"""
runing1 time: 0.303566 s
runing2 time: 1.365852 s
------------------------------------------------------------
runing1 time: 0.001498 s
runing2 time: 0.857026 s
------------------------------------------------------------
runing1 time: 0.001402 s
runing2 time: 0.284110 s
"""
