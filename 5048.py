# coding: utf-8
""" 5048. 拼写单词
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
注意：每次拼写时，chars 中的每个字母都只能用一次。
返回词汇表 words 中你掌握的所有单词的 长度之和。

示例一：
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释：
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
"""


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        words_count = 0
        # 先对 chars 构成字典
        from collections import Counter
        counter = Counter(chars)
        # 再对 words 的元素进行比对
        for word in words:
            temp = Counter(word)
            if not (temp - counter):
                words_count += len(word)
        return words_count


if __name__ == '__main__':
    s = Solution()
    words = ["hello", "world", "leetcode"]
    chars = "welldonehoneyr"
    print(s.countCharacters(words, chars))
