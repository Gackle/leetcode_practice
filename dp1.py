# coding: utf-8
""" 钢条切割问题
"""


class Solution():
    """ 递归版本
    """

    def cut(self, p, n):
        """
        :type p: List[int]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        q = -1
        for i in range(1, n+1):
            q = max(q, p[i] + self.cut(p, n-i))
        return q


class Solution2():
    """ 自顶向下备忘录版本
    """

    def cut_memo(self, p, n):
        q = -1
        if n == 0:
            self.r[n] = 0
        elif self.r[n] < 0:
            for i in range(1, n+1):
                q = max(q, p[i] + self.cut_memo(p, n-i))
            self.r[n] = q
        return self.r[n]

    def cut(self, p, n):
        """
        :type p: List[int]
        :type n: int
        :rtype: int
        """
        self.r = [-1]*(len(p))
        self.cut_memo(p, len(p)-1)
        return self.r[n]


class Solution3():
    """ 自底向上的动态规划法
    """
    def cut(self, p, n):
        self.r = [0, 1]
        for i in range(2, len(p)):
            q = -1
            for j in range(1, i+1):
                q = max(q, p[j] + self.r[i-j])
            self.r.append(q)
        return self.r[n]


def main():
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 4
    s = Solution3()
    print(s.cut(p, n))


if __name__ == "__main__":
    main()
