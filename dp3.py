# coding: utf-8
""" 过桥问题
DP 的区间模型

给定一个长度为n（n <= 1000）的字符串A，
求插入最少多少个字符使得它变成一个回文串

提示：
典型的区间模型，回文串拥有很明显的子结构特征：
   即当字符串X是一个回文串时，在X两边各添加一个字符’a’后，aXa 仍然是一个回文串
我们用d[i][j]来表示A[i…j]这个子串变成回文串所需要添加的最少的字符数，那么：
1. 对于 A[i] == A[j] 的情况，很明显有 d[i][j] = d[i+1][j-1] 
2. 对于 A[i] != A[j] 得情况，我们将它变成更小的子问题求解：
    a. 在A[j]后面添加一个字符A[i]
    b. 在A[i]前面添加一个字符A[j]
得到状态转移方程：
    d[i][j] = min(d[i+1][j] + 1, d[i][j-1] + 1)
"""


class Solution():
    def insert_palindrome(self, s):
        n = len(s)
        r = [[-1]*n for _ in range(n)]
        for i in range(n)[::-1]:
            r[i][i] = 0
            if i < n-1:
                r[i][i+1] = 1 if s[i] != s[i+1] else 0
            for j in range(i+2, n):
                r[i][j] = min(r[i+1][j] + 1, r[i][j-1] + 1)
        return r[0][n-1]


if __name__ == "__main__":
    s = Solution()
    string = "abbc"
    print(s.insert_palindrome(string))
