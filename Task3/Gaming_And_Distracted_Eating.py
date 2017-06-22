'''
A group of researchers are interested in the possible effects of distracting stimuli during eating,
such as an increase or decrease in the amount of food consumption. To test this hypothesis,
 they monitored food intake for a group of 44 patients who were randomised into two equal groups.
 The treatment group ate lunch while playing solitaire, and the control group ate lunch without any added distractions.
 Patients in the treatment group ate 52.1 grams of biscuits, with a standard deviation of 45.1 grams,
 and patients in the control group ate 27.1 grams of biscuits with a standard deviation of 26.4 grams.
 Do these data provide convincing evidence that the average food intake is different for the patients
 in the treatment group? Assume the conditions for inference are satisfied.

Null hypothesis is H0: u_t - u_c = 0, alpha is 0.05
'''

# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''

# from log_api import log

import math


class Solution():
    def solve(self):
        amount1 = 22
        amount2 = 22
        avg1 = 52.1
        stddev1 = 45.1
        avg2 = 27.1
        stddev2 = 26.4

        t = avg1 - avg2
        sw_squared = (math.pow(stddev1, 2) / amount1 + math.pow(stddev2, 2) / amount2)
        t = t / (math.sqrt(sw_squared))
        t_42 = 2.0181
        return [min(amount1 - 1, amount2 - 1), round(t, 2), not math.fabs(t) >= t_42]


s = Solution()
print(s.solve())
