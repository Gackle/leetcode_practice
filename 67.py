# coding: utf-8
''' 67. 二进制求和
'''


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        b = int(b, 2)
        return str(bin(a + b)).replace('0b', '')


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("11", "1"))
