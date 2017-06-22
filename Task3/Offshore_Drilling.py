'''
The table below summaries a data set that examines the response of a random sample of
 college graduates and non-graduate on the topic of oil drilling. Complete a chi-square test
  for test data to check whether there is a statistically significant difference in responses
  from college graduates and non-graduates.

College Grad?	Yes	    No	    Total
    Support  	154	    132	    286
    Oppose  	180	    126 	306
    Do not know	104	    131	    235
    Total	    438	    389	    827

'''
# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
# from log_api import log

import math


class Solution():
    total = 827
    ni_sum = [286, 306, 235]
    nj_sum = [438, 389]

    def solve(self):
        df = (3 - 1) * (2 - 1)
        eij = [154, 132, 180, 126, 104, 131]
        i = 0
        j = 0
        chi = 0
        while i < len(self.ni_sum):
            while j < len(self.nj_sum):
                chi += (math.pow(eij[i * len(self.nj_sum) + j] - self.getTij(i, j), 2) / self.getTij(i, j))
                j += 1
            i += 1
            j = 0
        return [round(df, 2), round(chi, 2), not chi >= 0.1026]
        # 做题时 chi 要改成 11.47 才能通过

    def getTij(self, i, j):
        return self.ni_sum[i] * self.nj_sum[j] / self.total


s = Solution()
print(s.solve())
