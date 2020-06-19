# -*- coding: utf-8 -*-
""" 125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 双指针
        s = s.upper()
        j = len(s) - 1
        i = 0
        while i <= j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    st = "0P"
    assert s.isPalindrome(st) is False
    st = "A man, a plan, a canal: Panama"
    assert s.isPalindrome(st) is True
    st = "race a car"
    assert s.isPalindrome(st) is False
