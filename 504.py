# coding: utf-8
""" 504. 七进制数
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"

示例 2:
输入: -7
输出: "-10"

注意: 输入范围是 [-1e7, 1e7] 。
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        flag = ""
        result = ""
        if num < 0:
            flag = "-"
            num = -num
        if num == 0:
            result = "0"

        while num > 0:
            bit = num % 7
            result = str(bit) + result
            num //= 7
        return flag + result


if __name__ == "__main__":
    s = Solution()
    assert s.convertToBase7(10) == "13", "10 != base7(13)"
    assert s.convertToBase7(100) == "202", "100 != base7(202)"
    assert s.convertToBase7(-7) == "-10", "-7 != base7(-10)"
    assert s.convertToBase7(int(1e7)) == "150666343", "1e7 != base7(150666343)"
