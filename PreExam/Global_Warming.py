'''
当前世界全球变暖现象严重，为了探索中国是否也存在这个现象，现调查了中国主要城市的全年气温情况，包括2010年全年气温状况与2014年全年气温状况，
以8月份气温为例，假设主要城市温度符合正态分布，试比较是否存在温度上升现象？（需给出证明过程，仅回答YES或NO不得分）
'''

# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
# from log_api import log

import requests
from scipy.stats import t
import math
import csv

# temperature_2010 = [25.7, 25.6, 25.6, 22.4, 21.7, 23.3, 23, 22.2, 27.9, 27.2, 28.4, 27.5, 29.3, 29.4, 25.1, 26, 29.1,
#                     29.4, 29.9, 28.8, 28.1, 28.4, 25, 23.6, 20.6, 16.4, 24.7, 18.3, 15.4, 21.3, 22.9]
# temperature_2014 = [27.3, 27.7, 27.9, 23.6, 20.6, 24.3, 22.6, 22.5, 31, 30.8, 31.3, 31.1, 29.6, 31.6, 28.6, 30.1, 30.6,
#                     32, 27.5, 27.7, 27.9, 30.5, 26.5, 23.1, 19.9, 15.9, 28.3, 21, 18.2, 24.4, 22.8]

url_2010 = 'http://py.mooctest.net:8081/dataset/temperature/temperature_2010.csv'
url_2014 = 'http://py.mooctest.net:8081/dataset/temperature/temperature_2014.csv'


class Solution():
    def solve(self):
        alpha = 0.05
        temperature_2010 = []
        temperature_2014 = []

        content_2010 = requests.get(url_2010)
        content_2010.encoding = 'gbk'
        f_csv_2010 = csv.reader(content_2010.text.split('\r\n'))
        for row in f_csv_2010:
            if len(row) == 14:
                if row[0] == '':
                    continue
                else:
                    if str(row[8]).replace(".", "").isdecimal():
                        temperature_2010.append(row[8])

        content_2014 = requests.get(url_2014)
        content_2014.encoding = 'gbk'
        f_csv_2014 = csv.reader(content_2014.text.split('\r\n'))
        for row in f_csv_2014:
            if len(row) == 14:
                if row[0] == '':
                    continue
                else:
                    if str(row[8]).replace(".", "").isdecimal():
                        temperature_2014.append(row[8])

        delta = [float(x) - float(y) for (x, y) in zip(temperature_2010, temperature_2014)]
        n = len(delta)
        avg = sum(delta) / n
        stddev = math.sqrt(sum([math.pow(x - avg, 2) for x in delta]) / n)
        t_val = avg / (stddev / math.sqrt(n))
        t_30 = t.ppf(alpha, 30)
        return 'YES' if not t_val > t_30 else 'NO'


s = Solution()
print(s.solve())
