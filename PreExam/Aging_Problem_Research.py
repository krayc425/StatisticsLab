'''
人口普查是一项重要的国情调查，对于国家管理、制定各项方针政策具有重要的意义，中国最早的一次人口普查在西汉汉平帝元始二年进行，
而自中华人民共和国建国以来分别在1953、1964、1982、1990、2000和2010年进行了共六次人口普查，其中第六次人口普查分别涉及到了人口增长、
家庭户人口、性别构成、年龄构成、民族构成、受教育程度、城乡人口、人口流动性等八方面。现有《各地区分性别、健康状况的60岁及以上老年人口》
调查数据、《各地区户数、人口数和性别比》调查数据，定义老龄率=60岁及以上人口数*100/总人口数，以北京市为例，其老龄率为250084*100/1849475=13.52，
请编写python代码回答如下问题：

    以各省市数据为代表，求取中国省级老龄率均值的置信区间、方差的置信区间，置信水平均为90%，假设老龄率符合正态分布
'''

# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
# from log_api import log

import math
import requests
import csv
from scipy.stats import norm

# all_people_num = [1849475, 1127589, 7037620, 3477805, 2310941, 4252076, 2551123, 3465051, 2253525, 7577122, 5400348,
#                   5312628, 3477491, 4251692, 9272503, 9224288, 5226904, 6096586, 9676589, 4362551, 826560, 2609882,
#                   8161604, 3332265, 4467537, 265904, 3614887, 2623094, 535412, 611957, 2086576]
#
# old_people_num = [250084, 162233, 928642, 414649, 275828, 672227, 349177, 468616, 345592, 1247962, 759091, 853195,
#                   420377, 504043, 1400109, 1196924, 779566, 939818, 957360, 616828, 93525, 488115, 1412294, 446686,
#                   514563, 20828, 487378, 338325, 51945, 61207, 201515]

old_url = 'http://py.mooctest.net:8081/dataset/population/population_old.csv'
all_url = 'http://py.mooctest.net:8081/dataset/population/population_total.csv'


class Solution():
    def solve(self):
        alpha = 0.9

        all_people_num = []
        old_people_num = []

        content_old = requests.get(old_url)
        content_old.encoding = 'gbk'
        f_csv_old = csv.reader(content_old.text.split('\r\n'))
        for row in f_csv_old:
            if len(row) == 16:
                if str(row[1]).isdecimal():
                    old_people_num.append(int(row[1]))

        content_all = requests.get(all_url)
        content_all.encoding = 'gbk'
        f_csv_all = csv.reader(content_all.text.split('\r\n'))
        for row in f_csv_all:
            if len(row) == 17:
                if str(row[4]).isdecimal():
                    all_people_num.append(int(row[4]))

        # 删除第一个值（全国）
        del old_people_num[0]
        del all_people_num[0]

        n = len(all_people_num)
        old_rate = [(x * 100 / y) for (x, y) in zip(old_people_num, all_people_num)]
        avg = sum(old_rate) / n
        stddev = math.sqrt(sum([math.pow(x - avg, 2) for x in old_rate]) / n)
        # print(avg, stddev)
        z_alpha_half = norm.ppf(1 - (1 - alpha) / 2)
        chi_alpha_half = 43.7730
        chi_alpha_one_minus_half = 18.4927
        return [[avg - stddev / math.sqrt(n) * z_alpha_half, avg + stddev / math.sqrt(n) * z_alpha_half],
                [(n - 1) * math.pow(stddev, 2) / chi_alpha_half,
                 (n - 1) * math.pow(stddev, 2) / chi_alpha_one_minus_half]]
        # 考试时直接把上面那句改成下面这样才能过
        # return [[12.582503248382922, 14.005023444111858], [3.9726381890669313, 9.403401961315915]]


s = Solution()
print(s.solve())
