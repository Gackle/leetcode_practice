# coding: utf-8
""" 46. 全排列
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

思路：回溯算法
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(nums, [])
        return self.result

    def dfs(self, rest, path):
        """
        :type rest: List[int]
        :type path: List[int]
        :rtype: None
        """
        if not rest:
            self.result.append(path[:])
            return
        len_rest = len(rest)
        for i in range(len_rest):
            current = rest.pop(i)
            path.append(current)
            self.dfs(rest, path)
            # 回滚剪枝
            path.pop()
            rest.insert(i, current)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.permute(nums))
