# coding: utf-8
""" 150. 逆波兰表达式求值

根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif i == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif i == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            elif i == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            else:
                stack.append(int(i))

        return stack[0] if stack != [] else 0


if __name__ == '__main__':
    s = Solution()
    tokens = ["4", "13", "5", "/", "+"]
    print(s.evalRPN(tokens))
