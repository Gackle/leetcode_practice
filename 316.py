# coding: utf-8
""" 316. 去除重复字母

给定一个仅包含小写字母的字符串，去除字符串中重复的字母，使得每个字母只出现一次。
需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1:

    输入: "bcabc"
    输出: "abc"

示例 2:

    输入: "cbacdcbc"
    输出: "acdb"
"""


class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        hashtable = collections.defaultdict(int)
        for c in s:
            hashtable[c] += 1

        stack = set()
        string = ""

        for c in s:
            if c not in stack:
                while string and string[-1] > c and hashtable[string[-1]]:
                    stack.remove(string[-1])
                    string = string[:-1]
                string += c
                stack.add(c)
            hashtable[c] -= 1
        return string


class Solution2:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        rindex = {c: i for i, c in enumerate(s)}
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result

if __name__ == "__main__":
    s = Solution()
    t = "bcabc"
    # t = "ccacbaba"
    # t = "cbacdcbc"
    t = "bddbccd"
    print(s.removeDuplicateLetters(t))
    # output "abc"
    # ouptut "acb"
    # output "acdb"
    # output "bcd"
