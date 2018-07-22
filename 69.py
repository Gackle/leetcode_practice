# coding: utf-8
''' 69. x 的平方根
'''


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        guess = x / 2
        while abs(guess**2 - x) > 0.5:
            guess = guess - (((guess**2) - x) / (2 * guess))
        return int(guess)


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(8))
