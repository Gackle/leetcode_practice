# coding: utf-8
""" 1106. 解析布尔表达式
给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。

有效的表达式需遵循以下约定：

"t"，运算结果为 True
"f"，运算结果为 False
"!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
"&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
"|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）

示例 1：
输入：expression = "!(f)"
输出：true

示例 2：
输入：expression = "|(f,t)"
输出：true

示例 3：
输入：expression = "&(t,f)"
输出：false

示例 4：
输入：expression = "|(&(t,f,t),!(t))"
输出：false
"""


class Solution(object):
    def __init__(self):
        self.ex_s = list()

    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        self.ex = expression
        i = 0
        self.add_op(i+1, expression[0], 0)
        return self.ex_s[-1]

    def add_op(self, i, op, ex_index):
            while i < len(self.ex) and self.ex[i] != ")":
                if self.ex[i] in ("&", "|", "!"):
                    i = self.add_op(i+1, self.ex[i], len(self.ex_s))
                elif self.ex[i] == 't':
                    self.ex_s.append(True)
                elif self.ex[i] == 'f':
                    self.ex_s.append(False)
                i += 1
            if op == '&':
                co = all(self.ex_s[ex_index:])
                self.ex_s = self.ex_s[:ex_index]
            elif op == '|':
                co = any(self.ex_s[ex_index:])
                self.ex_s = self.ex_s[:ex_index]
            else:
                p = self.ex_s.pop()
                co = not p
            self.ex_s.append(co)
            return i

if __name__ == '__main__':
    s = Solution()
    assert s.parseBoolExpr("!(f)")
    assert s.parseBoolExpr("|(f,t)")
    assert not s.parseBoolExpr("&(t,f)")
    assert not s.parseBoolExpr("|(&(t,f,t),!(t))")
    assert s.parseBoolExpr("!(&(!(t),&(f),|(f)))")
    assert not s.parseBoolExpr("!(&(!(&(f)),&(t),|(f,f,t)))")
    print("All passed!")
