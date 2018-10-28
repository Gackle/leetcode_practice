# coding: utf-8
""" 76. 最小覆盖子串
给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。
[双指针 哈希表 字符串]

示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

说明：
+ 如果 S 中不存这样的子串，则返回空字符串 ""。
+ 如果 S 中存在这样的子串，我们保证它是唯一的答案。

注意，t 中重复出现的字母，在子串中也要重复相同遍数
"""


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        import collections
        # t 中每个字符出现的次数，作为哈希表使用
        d = collections.Counter(t)
        # t 中字符个数，即需要匹配的字符个数
        missing = len(t)
        # 子串开始和结束位置
        begin = -1
        end = len(s)
        # 左指针起始位置
        left = 0
        for right, value in enumerate(s):
            # 右指针往后遍历
            missing -= 1 if d[value] > 0 else 0
            # 每个对应字符（包含非匹配）的出现次数减一
            d[value] -= 1
            # 当右指针遍历得到一个合符条件的子串，即 missing 清零
            if not missing:
                # 左指针需要往右走，压缩子串
                while left < right and d[s[left]] < 0:
                    # 跳过不应该匹配的字符，他们的匹配出现次数会小于0（因为默认为 0）
                    d[s[left]] += 1
                    left += 1
                # 找到新的子串开始位置，且比 min_len 最小长度要小
                if right - left <= end - begin:
                    begin, end = left, right

        # 如果子串起始位置未改变，即没有找到对应的子串
        return "" if begin == -1 else s[begin: end + 1]


if __name__ == "__main__":
    S = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(S.minWindow(s, t))
