# coding: utf-8
""" 866. 回文素数

求出大于或等于 N 的最小回文素数。

提示：

- 1 <= N <= 10^8
- 答案肯定存在，且小于 2 * 10^8。
"""


class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        while not self.__isPalindrome(N) or not self.__isPrim(N):
            N += 1
            if N > 10**1 and N < 10**2 and N != 11:
                N = 10**2
            if N > 10**3 and N < 10 ** 4:
                N = 10**4
            if N > 10**5 and N < 10**6:
                N = 10**6
            if N > 10**7 and N < 10**8:
                N = 10**8
            if N % 2 == 0 and N != 2:
                N += 1
        return N

    def __isPrim(self, N):
        if N == 1:
            return False
        import math
        i = 2
        while i <= math.sqrt(N):
            if N % i == 0:
                return False
            i += 1
        return True

    def __isPalindrome(self, N):
        return str(N) == str(N)[::-1]


if __name__ == "__main__":
    s = Solution()
    N = 3503054
    print(s.primePalindrome(N))
