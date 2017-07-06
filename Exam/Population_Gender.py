'''
人口普查是一项重要的国情调查，对于国家管理、制定各项方针政策具有重要的意义，中国最早的一次人口普查在西汉汉平帝元始二年进行，而自中华人民
共和国建国以来分别在1953、1964、1982、1990、2000和2010年进行了共六次人口普查，其中第六次人口普查分别涉及到了人口增长、家庭户人口、
性别构成、年龄构成、民族构成、受教育程度、城乡人口、人口流动性等八方面。现有关于《各地区分性别、孩次的出生人口（2009.11.-2010.10.31）》
的数据，请利用Python代码完成如下问题：

1）以各省市数据为代表，假设中国出生人口的性别比不符合正态分布，求取中国出生人口的性别比的均值的置信区间（置信水平90%）

2）以各省市数据为代表，为了探索是否存在“重男轻女”现象，试求取第一胎和非第一胎的出生人口的性别比的均值差的范围（注意：非第一胎减第一胎，
置信水平90%，假设第一胎与非第一胎是独立的，并且第一胎与非第一胎出生人口性别比均不符合正态分布）
'''

# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
# from log_api import log

import math
import scipy.stats as stats

gender_ratio = [112.15, 114.59, 118.71, 113.07, 108.87, 112.91, 115.67, 115.1, 111.49, 121.38, 118.36, 131.07, 125.71,
                128.27, 124.28, 127.64, 123.94, 125.78, 129.49, 122, 129.43, 113.8, 112.98, 126.2, 113.61, 100.08,
                116.1, 124.79, 112.69, 114.36, 105.56]
first_child_b = [5739, 3418, 23654, 9455, 7140, 9590, 6298, 8951, 6687, 23157, 15543, 19417, 12114, 11968, 30616, 27263,
                 19467, 20923, 31282, 16506, 2947, 6419, 19224, 11080, 14577, 598, 10590, 7792, 1661, 1966, 7648]
first_child_g = [5348, 3058, 21704, 8404, 6653, 8679, 5408, 7730, 6288, 20176, 14168, 17182, 10749, 10508, 27000, 23094,
                 16927, 17462, 25579, 14402, 2514, 5736, 16912, 10129, 13388, 555, 9255, 6595, 1540, 1833, 7200]
all_child_b = [6879, 4572, 41736, 15617, 10387, 12519, 8328, 11200, 8598, 34825, 24654, 31594, 19173, 25679, 46753,
               51936, 29647, 36869, 53596, 30889, 5805, 10333, 31499, 20685, 26023, 1284, 16265, 13717, 3143, 3648,
               14220]
all_child_g = [6134, 3990, 35157, 13812, 9541, 11088, 7200, 9731, 7712, 28690, 20829, 24104, 15252, 20019, 37620, 40690,
               23921, 29313, 41389, 25318, 4485, 9080, 27881, 16391, 22906, 1283, 14009, 10992, 2789, 3190, 13471]


class Solution():
    def solve(self):
        gender_ratio_n = len(gender_ratio)
        gender_ratio_avg = sum(gender_ratio) / len(gender_ratio)
        gender_ratio_stddev = math.sqrt(
            sum([math.pow(x - gender_ratio_avg, 2) for x in gender_ratio]) / len(gender_ratio))

        mean = [gender_ratio_avg - gender_ratio_stddev / math.sqrt(gender_ratio_n) * 1.65,
                gender_ratio_avg + gender_ratio_stddev / math.sqrt(gender_ratio_n) * 1.65]

        not_first_b = [x - y for (x, y) in zip(all_child_b, first_child_b)]
        not_first_g = [x - y for (x, y) in zip(all_child_g, first_child_g)]
        first_ratio = [100 * float(x) / float(y) for (x, y) in zip(first_child_b, first_child_g)]
        not_first_ratio = [100 * float(x) / float(y) for (x, y) in zip(not_first_b, not_first_g)]

        avg_first = sum(first_ratio) / len(first_ratio)
        stddev_first = math.sqrt(sum([math.pow(x - avg_first, 2) for x in first_ratio]) / len(first_ratio))
        avg_not_first = sum(not_first_ratio) / len(not_first_ratio)
        stddev_not_first = math.sqrt(
            sum([math.pow(x - avg_not_first, 2) for x in not_first_ratio]) / len(not_first_ratio))
        delta = math.sqrt(stddev_first ** 2 / len(first_ratio) + stddev_not_first ** 2 / len(not_first_ratio))
        var = [avg_not_first - avg_first - delta * stats.norm.ppf(0.95),
               avg_not_first - avg_first + delta * stats.norm.ppf(0.95)]
        return [mean, var]


s = Solution()
print(s.solve())
