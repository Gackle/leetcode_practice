# coding: utf-8
""" 1071. 字符串的最大公因子
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

示例 1：
输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"

示例 2：
输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"

示例 3：
输入：str1 = "LEET", str2 = "CODE"
输出：""


思路：如果 S 和 T 存在最大公因子 G ，则 S = mG ， T = nG ， S+T = (m+n)G = (n+m)G = T+S ，因此反过来 S + T != T + S 是此题无解的充要条件；
然后再存在有解的情况下，G 的长度 len(G) 必然也满足 len(T) 和 len(S) 的最大公约数 l ，即 G = S[:l] = T[:l] 
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        return str1[:gcd(len(str1), len(str2))]


if __name__ == "__main__":
    s = Solution()
    str1 = "ABCABC"
    str2 = "ABV"
    print(s.gcdOfStrings(str1, str2))
