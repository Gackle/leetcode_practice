# coding: utf-8
""" 394. 字符串解码

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

示例：
    s = "3[a]2[bc]", 返回 "aaabcbc".
    s = "3[a2[c]]", 返回 "accaccacc".
"""


class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        stack_char = []
        stack_number = []
        i = 0
        while i < len(s):
            if s[i] == "[":
                # 遇到 [，进行入栈操作
                j = i - 1
                number_bulider = []
                k = i + 1
                char_bulider = []
                # 数字入栈
                while j >= 0 and s[j].isdigit():
                    number_bulider.insert(0, s[j])
                    j -= 1
                stack_number.append(int(''.join(number_bulider)))
                # 字符入栈
                while s[k].isalpha():
                    char_bulider.append(s[k])
                    k += 1
                stack_char.append(''.join(char_bulider))
                i = k
                continue
            elif s[i] == "]":
                # 遇到 ]，进行出栈操作
                char = stack_char.pop()
                number = stack_number.pop()
                string = char * number
                if len(stack_char) == 0:
                    output += string
                else:
                    stack_char[-1] += string
            elif s[i].isalpha():
                # 遇到孤立的字符，直接认为做出栈处理
                if len(stack_char) == 0:
                    output += s[i]
                else:
                    stack_char[-1] += s[i]
            i += 1
        return output


if __name__ == '__main__':
    s = Solution()
    # string = "3[a2[c]]"
    string = "3[a]2[b4[F]c]"
    # string = "2[abc]3[cd]ef"
    # string = "ef"
    # string = "3[ab2[c4[d]]]ef5[g]"
    print(s.decodeString(string))
