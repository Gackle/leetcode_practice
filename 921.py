# coding: utf-8
""" 921. 使括号有效的最小添加
给定一个由 '(' 和 ')' 括号组成的字符串 S，我们需要添加最少的括号（ '(' 或是 ')'，可以在任何位置），以使得到的括号字符串有效。
从形式上讲，只有满足下面几点之一，括号字符串才是有效的：
- 它是一个空字符串，或者
- 它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者
- 它可以被写作 (A)，其中 A 是有效字符串。

给定一个括号字符串，返回为使结果字符串有效而必须添加的最少括号数。

示例 1：
输入："())"
输出：1

示例 2：
输入："((("
输出：3

示例 3：
输入："()"
输出：0

示例 4：
输入："()))(("
输出：4

提示：栈 贪心算法
"""


class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        result = 0
        # 栈实现
        stack = list()
        for i in S:
            if i == "(":
                stack.append("(")
                result += 1
            else:
                if stack:
                    stack.pop()
                    result -= 1
                else:
                    result += 1
        return result


class Solution2(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0
        left = 0
        ans = 0
        # 贪心算法
        for i in S:
            if i == "(":
                left += 1
            elif left:
                left -= 1
            else:
                ans += 1
        return left + ans


if __name__ == "__main__":
    s = Solution2()
    S = "()))(("
    print(s.minAddToMakeValid(S))
