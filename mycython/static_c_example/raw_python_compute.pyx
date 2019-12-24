# coding=utf-8
# 第一个方法可以计算地球表面任意两个经纬度之间的距离，这个方法使用了很多三角函数，这些三角函数由python的math模块提供
# 第二个方法就是纯数字的计算

import math
def spherical_distance(lon1, lat1, lon2, lat2):
    radius = 3956
    x = math.pi/180.0
    a = (90.0 - lat1)*x
    b = (90.0 - lat2)*x
    theta = (lon2 - lon1)*x
    distance = math.acos(math.cos(a)*math.cos(b)) + (math.sin(a) * math.sin(b) * math.cos(theta))
    return radius * distance

def f_compute(a, x, N):
    s = 0
    dx = (x - a)/N
    for i in range(N):
        s += ((a + i * dx) ** 2 - (a + i * dx))
    return s * dx