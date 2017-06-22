# -*- coding:utf-8 -*-

class Solution():
    def solve(self, A):
        result = []
        for string in A:
            if self.isPalindrome(string):
                result.append(string)
        return result

    def isPalindrome(self, x):
        i = 0
        xString = str(x)
        while i < len(xString):
            if xString[i] != xString[len(xString) - i - 1]:
                return False
            i += 1
        return True


p = Solution()
print(p.solve(['123', '232', '4556554', '12123', '3443', '1314131']), end="")
