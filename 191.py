# coding: utf-8
""" 191. 位1的个数

编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')


if __name__ == '__main__':
    s = Solution()
    n = 128
    print(s.hammingWeight(n))
