'''
假定一块蛋糕上的葡萄干粒数服从泊松分布，如果想让每块蛋糕上至少有一粒葡萄干的概率大于等于0.98，蛋糕上葡萄干的平均粒数应该是多少？
'''

# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
# from log_api import log

import scipy.stats as stats
import math


class Solution():
    def solve(self):
        result = 0
        p = 0.02
        while math.pow(math.e, -result) > p:
            result += 1
        return result
        # 或者使用下面方法：用统计包内置泊松分布
        # n = 0
        # while stats.poisson.pmf(0, n) >= p:
        #     n += 1
        # return n


s = Solution()
print(s.solve())
