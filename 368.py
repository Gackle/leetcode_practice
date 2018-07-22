# coding: utf-8
''' 368. 最大整除子集

给出一个由无重复的正整数组成的集合, 找出其中最大的整除子集, 子集中任意一对 (Si, Sj) 都要满足: Si % Sj = 0 或 Sj % Si = 0。

如果有多个目标子集，返回其中任何一个均可。
'''


class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == [] or nums is None:
            return []
        # 状态转移方程
        import threading
        

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.largestDivisibleSubset(nums))
