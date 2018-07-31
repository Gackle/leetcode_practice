# coding: utf-8
'''
326. 3的幂

给定一个整数，写一个函数来判断它是否是 3 的幂次方
'''


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        # import math
        # return math.log(n, 3) % 1 == 0
        return 3**19 % n == 0


if __name__ == '__main__':
    s = Solution()
    n = 243
    print(s.isPowerOfThree(n))
