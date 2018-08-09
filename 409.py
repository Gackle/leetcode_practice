# coding: utf-8
""" 409. 最长回文串

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

思路：偶数个个数的字符可以直接放入到回文字符串中，奇数个个数的字符如果可以变为偶数的话也可以进行 -1 操作之后放入回文字符串中；
因此需要哈希表来记录全部字符出现的次数再进行处理
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashtable = [0] * 52
        for i in s:
            n = ord(i)
            if n > 96:
                # 小写字母
                hashtable[n - 71] += 1
            else:
                # 大写字母
                hashtable[n - 65] += 1

        count = 0
        need_add_one = False
        # 处理哈希表
        for i in hashtable:
            if i % 2 == 0:
                # 偶数个数
                count += i
            else:
                count += i - 1
                need_add_one = True

        return count + 1 if need_add_one else count


if __name__ == '__main__':
    s = Solution()
    string = "abccccdd"
    print(s.longestPalindrome(string))
