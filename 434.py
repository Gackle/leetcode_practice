# coding: utf-8
''' 434. 字符串中的单词数

统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。
'''


class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        string = ""
        for i in s:
            if ord(i) != 32:
                string += i
            else:
                if string != "":
                    count += 1
                    string = ""
                else:
                    continue
        return count if string == "" else count + 1

    def countSegments2(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        data = s.split()
        return (len(data))


if __name__ == '__main__':
    s = Solution()
    # string = "Hello, my name is John"
    string = "Whatever is worth doing is worth doing well."
    print(s.countSegments2(string))
