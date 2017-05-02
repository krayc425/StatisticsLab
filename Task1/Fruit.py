# -*- coding:utf-8 -*-

# 已知列表fruits中顺序保存了某商店每日出售的水果品名，例如fruits=['apple','banana','cherry','pineapple','banana','peach','pear','peach','cherry' ]，完成函数solve()计算每一种水果的出售次数，存入字典result中并将结果返回

class Solution():
    def solve(self, A):
        result = {}
        for string in A:
            i = 0
            if string in result:
                result[string] += 1
            else:
                result[string] = 1
            i += 1
        return result

s = Solution()
print(s.solve(['apple', 'banana', 'cherry', 'pineapple', 'banana', 'peach', 'pear','peach', 'cherry' ]))
