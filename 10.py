# -*- coding: utf-8 -*-
""" 10. 正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的
正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串 。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 * 。

思路：正则表达式 / 有限状态机（FSM）
"""


class Solution:
    """ 正则表达式解法
    """

    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if not s and len(p) == 1:
            return False

        m, n = len(s), len(p)
        # dp[i][j] 表示 s 的前 i 个字符和 p 的前 j 个字符「匹配」

        # 重点：初始化
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 空字符 s 和空字符 p 是匹配的，注意这里的 0 不等于下标，因为 Python List 从 0 开始
        dp[0][0] = True
        # 当 p 中存在 * 号时，在对于 dp[0][j] 存在 dp[0][j] = dp[0][j-2] 即将 []* 整体丢弃
        for c in range(2, n+1):
            j = c-1
            if p[j] == '*':
                dp[0][c] = dp[0][c-2]

        # 状态转移方程
        for r in range(1, m+1):
            i = r-1
            for c in range(1, n+1):
                j = c-1
                if s[i] == p[j] or p[j] == '.':
                    # 1. s[i] == p[j] ，则 dp[i][j] == dp[i-1][j-1]
                    # 2. p[j] == '.' 万能字符，则 dp[i][j] == dp[i-1][j-1]
                    dp[r][c] = dp[r-1][c-1]
                elif p[j] == '*':
                    # 3. p[j] == '*' ， 分两种情况
                    if p[j-1] == s[i] or p[j-1] == '.':
                        # 3.1 匹配了一次 []* 或多次 []*
                        dp[r][c] = dp[r-1][c] or dp[r][c-2]
                    else:
                        # 3.2 匹配了 0 次 []* ，整体丢弃
                        dp[r][c] = dp[r][c-2]
                else:
                    dp[r][c] = False

        return dp[m][n]


if __name__ == "__main__":
    S = Solution()
    s = "aa"
    p = "a"
    assert S.isMatch(s, p) is False, "case 1"
    s = "aa"
    p = "a*"
    assert S.isMatch(s, p) is True, "case 2"
    s = "ab"
    p = ".*"
    assert S.isMatch(s, p) is True, "case 3"
    s = "aab"
    p = "c*a*b"
    assert S.isMatch(s, p) is True, "case 4"
    s = "mississippi"
    p = "mis*is*p*."
    assert S.isMatch(s, p) is False, "case 5"
