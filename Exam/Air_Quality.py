# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
# from log_api import log

'''
为了探索中国空气质量情况，现调查了主要城市的空气质量情况，包括2010年环保重点城市空气质量情况与2014年环保重点城市空气质量情况，
以全年空气质量达到及好于二级的天数为例，试比较是否存在空气质量变差的现象，并给出检验统计量的值，alpha=0.05，使用配对数据检验方法
'''

import math
import scipy.stats as stats

air_2010 = [285, 307, 318, 296, 346, 328, 340, 311, 334, 315, 327, 321, 353, 347, 295, 322, 301, 333, 347, 362, 365,
            303, 315, 347, 365, 361, 304, 236, 280, 328, 262]
air_2014 = [167, 145, 49, 162, 213, 215, 230, 239, 246, 198, 212, 180, 343, 230, 79, 134, 161, 196, 259, 275, 342, 207,
            139, 278, 329, 341, 157, 193, 216, 249, 184]


class Solution():
    def solve(self):
        delta = [float(x) - float(y) for (x, y) in zip(air_2014, air_2010)]
        n = len(delta)
        avg = sum(delta) / n
        stddev = math.sqrt(sum((x - avg) ** 2 for x in delta) / (n - 1))    # 这咋就 n - 1 了我也不知道
        t_val = avg / (stddev / math.sqrt(n))
        t_30 = stats.t.ppf(0.95, 30)
        return [t_val, 'YES' if not t_val > t_30 else 'NO']


s = Solution()
print(s.solve())
