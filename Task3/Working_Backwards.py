'''
A 95% confidence interval for a population mean, u, is given as (18.985, 21.015). This confidence interval is based on a simple random
samples of 36 observations. Calculate the sample mean and standard deviation. Assume that all conditions necessary for inference are
satisfied. Use the t-distribution in any calculations.

'''
# -*- coding:utf-8 -*-
# from log_api import log
import math


class Solution():
    def solve(self):
        amount = 36
        x_lower = 18.985
        x_upper = 21.015
        average = (x_lower + x_upper) / 2
        standard_variation = (average - x_lower) / 2.03 * math.sqrt(amount)  # 2.03 is t(35, 0.05)
        return [round(average, 2), round(standard_variation, 2)]


s = Solution()
print(s.solve())
