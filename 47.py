# coding: utf-8
""" 47. 全排列Ⅱ
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

提示：
回溯算法
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def dfs(start, l):
            """
            :type start: int
            :type nums: List[int]
            :type l: List[int]
            """
            pass


class Solution1(object):
    """ 非回溯实现，但是非常有意思
    """
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return [nums]
        result = []
        existed = []
        for i, x in enumerate(nums):
            # 依次选取值作为排列的开头
            if x in existed:
                continue
            existed.append(x)
            # 将对应的值提取到队列开头，重排剩余部分
            rest = nums[:i] + nums[i+1:]
            if len(rest) > 0:
                # 求剩余部分的全排列
                for l in self.permuteUnique(rest):
                    result.append([x] + l)
        return result


if __name__ == "__main__":
    s = Solution1()
    nums = [1, 1, 2]
    print(s.permuteUnique(nums))
