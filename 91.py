# coding: utf-8
""" 91. 解码方法
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:
输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

示例 2:
输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

提示：动态规划

思路：这是一个典型的 f[n] = f[n-1] + f[n-2]，但是存在着约束关系。
我们从倒数两位出发，假如前 n-2 位有 f[n-2] 种解码，n-1 位有 f[n-1] 种解码；
则最后两位如果可以继续拆分，则明显有 f[n-2]+f[n-1] 种解码；如果不能拆分，则明显有 f[n-1] 种解码，
对于字符串长度 n，有以下状态转移方程：
    f[n] = f[n-1] + f[n-2], f[n] 表示当前长度 n 存在 f[n] 种拆分方法，
以上情况，对于 s[n-2:n] < 26 时成立
约束情况：
1. 如果 s[n-2:2] > 26 或者后两位数种包括一个 0 且前它前一位为 1 或者 2，则只有 f[n-1] 种拆分方法
2. 如果 s[n] 为 0 且前一位不为 1 或者 2，则解码失败

注意：题目没有明说，但实际上用例包括 0
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 边界处理
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        # dp 处理
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] != '1' and s[i-1] != '2':
                    return 0
                else:
                    dp[i] = dp[i-2]
                    continue
            if s[i-1] == '0' or int(s[i-1:i+1]) > 26:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


class Solution1:
    """ 提交最快解法
    """
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0 for _ in range(n)]

        if n == 1 and s[0] != '0':
            return 1
        if s[0] == '0':
            return 0
        else:
            dp[0] = 1
        for i in range(1, n):

            rec = int(s[i-1] + s[i])

            if s[i] == '0':
                if 1 > rec or rec > 26:
                    return 0
                elif i > 2:
                    dp[i] = dp[i-2]
                else:
                    dp[i] = 1

            elif 1 <= rec <= 26 and s[i-1] != '0':
                if i > 2:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i-1]
        return dp[n-1]


if __name__ == "__main__":
    s = Solution()
    string = "20"
    print(s.numDecodings(string))
