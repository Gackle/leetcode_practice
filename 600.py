# coding: utf-8
""" 600. 不含连续1的非负整数
给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含连续的 1 的个数。

示例 1:

输入: 5
输出: 5
解释:
下面是带有相应二进制表示的非负整数<= 5：
    0 : 0
    1 : 1
    2 : 10
    3 : 11
    4 : 100
    5 : 101
其中，只有整数 3 违反规则（有两个连续的1），其他5个满足规则。
说明: 1 <= n <= 109
"""


class Solution:
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        pass


if __name__ == '__main__':
    s = Solution()
    num = 5
    print(s.findIntegers(num))
