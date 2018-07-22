# coding: utf-8


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
