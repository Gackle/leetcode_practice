# coding: utf-8
""" 77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

提示：回溯算法
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.result = list()
        end = n+2-k
        for i in range(1, end):
            self.dfs(i+1, end+1, k-1, [i])
        return self.result

    def dfs(self, start, n, k, current):
        """ 深度搜索
        :type start: int
        :type n: int
        :param n: 该轮遍历的终点
        :type k: int
        :param k: 第 k 轮遍历（倒序）
        :type current: List[int]
        """
        if k == 0:
            self.result.append(current)
            return
        for i in range(start, n):
            temp = current[:]
            temp.append(i)
            self.dfs(i+1, n+1, k-1, temp)


class SolutionFast(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        import itertools
        return itertools.combinations(range(1, n+1), k)

if __name__ == "__main__":
    s = SolutionFast()
    n = 4
    k = 2
    print(s.combine(n, k))
