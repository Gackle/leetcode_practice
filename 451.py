# coding: utf-8
""" 451. 根据字符出现频率排序

给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
"""


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        counter = Counter(s)
        return_value = ""
        for k, v in sorted(counter.items(), key=lambda x: x[1], reverse=True):
            return_value += k * v
        return return_value


if __name__ == '__main__':
    s = Solution()
    string = "tree"
    print(s.frequencySort(string))
