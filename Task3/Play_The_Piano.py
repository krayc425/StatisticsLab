'''
 Georgianna claims that in a small city renowned for its music school,
 the average child takes at least 5 years of piano lessons. We have a random sample of 20 children from the city
  with a mean of 4.6 years of piano lessons and a standard deviation of 2.2 years. Evaluate Georgianna's claims
   using a hypothesis test. alpha is 0.05.


Extra:

(1) Construct a 95% confidence interval for the number of years students in this city takes piano lessons
 and interpret it in context of the data.

(2) Do your results from the hypothesis test and the confidence interval agree? Explain your reasoning.
'''
# -*- coding:utf-8 -*-
# from log_api import log

import math


class Solution():
    def solve(self):
        avg = 4.6
        amount = 20
        stddev = 2.2
        t = (avg - 5.0) / (stddev / math.sqrt(amount))
        t_19 = 1.7291
        return [round(amount - 1, 2), round(t, 2), not t <= -t_19]


s = Solution()
print(s.solve())
