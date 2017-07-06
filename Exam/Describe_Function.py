'''
利用python实现简化版描述函数

注意事项：

1）不能调用math、scipy、numpy包

2）为了使正态分布峰度为0，此处对峰度值做减3处理

3）当输入数据仅包含一个元素时，方差返回None


'''

# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''


# from log_api import log

class Solution():
    def solve(self, a):
        n = len(a)
        mean = float(sum(a)) / n
        var = float(sum([(float(x) - mean) ** 2 for x in a])) / float(n - 1) if n > 1 else None
        skew = (float(sum([(float(x) - mean) ** 3 for x in a])) / n) / float(
            (float(sum([(float(x) - mean) ** 2 for x in a])) / n) ** 1.5) if n > 1 else 0
        kurt = (float(sum([(float(x) - mean) ** 4 for x in a])) / n) / float(
            (float(sum([(float(x) - mean) ** 2 for x in a])) / n) ** 2) - 3 if n > 1 else -3
        return [mean, var, skew, kurt]


s = Solution()
print(s.solve([1]))
