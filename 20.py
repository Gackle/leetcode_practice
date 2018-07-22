# coding: utf-8
''' 20. 有效的括号
'''


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenthesis_stack = []
        bracket_stack = []
        brace_stack = []
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')' or c == ']' or c == '}':
                if len(stack) <= 0:
                    return False
                else:
                    t = stack.pop()
                    if t == "(" and c == ")" or t == "[" and c == "]" or t == "{" and c == "}":
                        continue
                    else:
                        return False

        return True if len(stack) == 0 else False


if __name__ == '__main__':
    s = Solution()
    s_str = "]"
    print(s.isValid(s_str))
