'''
New York is known as "the city that never sleeps".
A random sample of 25 New Yorkers were asked how much sleep they get per night.
Statistical summaries of these data are shown below. Do these data provide strong evidence
 that New Yorkers sleep less than 8 hours per night on average?

Null-hypothesis is H0: u=8, and alpha is 0.05

n	mean	stand-variance	min	max
25	7.73	0.77	6.17	9.78

Extra:

(1) If you were to construct a 90% confidence interval that corresponded to this hypothesis test,
 would you expect 8 hours to be in the interval? Explain your reasoning.
'''

# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
import math


class Solution():
    def solve(self):
        amount = 25
        avg = 7.73
        stddev = 0.77
        t = (avg - 8) / (stddev / math.sqrt(amount))
        t_24 = 1.3178
        return [round(amount - 1, 2), round(t, 2), not t <= -t_24]


s = Solution()
print(s.solve())
