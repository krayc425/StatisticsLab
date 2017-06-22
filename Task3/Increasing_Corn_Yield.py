'''
A large farm wants to try out a new type of fertilizer to evaluate whether it will improve the farm's corn production.
 The land is broken into plots that produce an average of 1.215 pounds of corn with a standard deviation of 94 pounds per plot.
 The owner is interested in detecting any average difference of at least 40 pounds per plot.
 How many plots of land would be needed for the experiment if the desired power level is 90%?
 Assume each plot of land gets treated with either the current fertilizer or the new fertilizer.
'''
# -*- coding:utf-8 -*-
# from log_api import log

import math


class Solution():
    def solve(self):
        stddev = 94
        n = 1
        while 40 / math.sqrt(2 * math.pow(stddev, 2) / n) < (1.28 + 1.96):
            n += 1
        return n


s = Solution()
print(s.solve())
