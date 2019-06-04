# coding: utf-8
""" 49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：
所有输入均为小写字母。
不考虑答案输出的顺序。

思路：
哈希表（对 Python 来说，可以直接使用 set）

在美版leetcode上看到大神的思路，用质数表示26个字母，把字符串的各个字母相乘，这样可保证字母异位词的乘积必定是相等的。其余步骤就是用map存储，和别人的一致了。（这个用质数表示真的很骚啊！！!）
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        for s in strs:
            st = ''.join(sorted(s))
            if st in d:
                d[st].append(s)
            else:
                d[st] = [s]
        return list(d.values())


if __name__ == "__main__":
    s = Solution()
    l = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(l))
