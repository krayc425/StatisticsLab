# -*- coding:utf-8 -*-

# 完成函数solve，判断传入的整数列表A中的数字是否是素数，并将所有的素数保存到另一个列表中并返回

class Solution():
    def solve(self, A):
        # call function prime
        result = []
        for num in A:
            if self.prime(num):
                result.append(num)
        return result

    # judge whether x is prime or not
    def prime(self, x):
        if x == 0 or x == 1:
            return False
        i = 2
        while i < x / 2:
            if x % i == 0:
                return False
            i += 1
        return True

s = Solution()
print(s.solve([1, 2, 23, 24, 25]))