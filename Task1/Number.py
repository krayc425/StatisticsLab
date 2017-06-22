# -*- coding:utf-8 -*-

# 已知有一个由数字字符串构成的列表，统计列表中数字字符'0'-'9'各自出现的次数并返回统计结果

class Solution():
    def solve(self, A):
        result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for string in A:
            i = 0
            while i < len(string):
                result[int(string[i])] += 1
                i += 1
        return result


s = Solution()
print(s.solve(['12', '34', '567', '36', '809', '120']))
