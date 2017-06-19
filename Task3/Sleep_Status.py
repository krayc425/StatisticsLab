'''
随着中国经济发展，人们生活质量相应提升，但睡眠质量却并不乐观。据《2016中国睡眠指数报告》显示，中国人平均睡眠时长为8.5小时，这是从3600份问卷统计得到的结果。
另外报告指出，中国人睡眠时长符合方差为25的正态分布，试写solve函数估计中国人睡眠时长的置信区间(置信水平为95%)
'''

# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
import math


# from log_api import log


def normal_distribution(self, x, ave, std):
    result = 1 / (math.sqrt(2 * math.pi) * std)
    p = - math.pow((x - ave), 2) / (2 * math.pow(std, 2))
    result *= (math.pow(math.e, p))
    return result


class Solution:
    def solve(self):
        average = 8.5
        amount = 3600
        standard_variation = 5
        return [average - 1.96 * standard_variation / math.sqrt(amount),
                average + 1.96 * standard_variation / math.sqrt(amount)]


s = Solution()
print(s.solve())
