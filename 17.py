# coding: utf-8
""" 17. 电话号码的字母组合

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.telephone = [(),
                          ('*',),
                          ('a', 'b', 'c'),
                          ('d', 'e', 'f'),
                          ('g', 'h', 'i'),
                          ('j', 'k', 'l'),
                          ('m', 'n', 'o'),
                          ('p', 'q', 'r', 's'),
                          ('t', 'u', 'v'),
                          ('w', 'x', 'y', 'z')]
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(self.telephone[int(digits[0])])
        else:
            return self.dfs(0, digits)

    def dfs(self, i, digits):
        """
        :type i: int
        :type digits: str
        """
        if i == len(digits) - 1:
            return [x for x in self.telephone[int(digits[i])]]
        output = []
        for tail in self.dfs(i + 1, digits):
            for n in self.telephone[int(digits[i])]:
                output.append(n + tail)
        return output


if __name__ == "__main__":
    s = Solution()
    digits = "23"
    digits = "9234"
    print(s.letterCombinations(digits))
