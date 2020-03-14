# coding: utf-8
""" 300. 最长上升子序列
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。

思路：动态规划解法：
对于数组 nums ，定义 dp[i] 为考虑前 i 个元素，以第 i 个数字结尾的最长上升子序列的长度，注意 nums[i] 必须被选取。
则存在状态转移方程 dp[j] = max(dp[i]) + 1 ，其中 0<i<j 且 num[j]>=num[i]，则所求值为 max(dp[i])， 其中 0<=i<len(nums)
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1]
        for i in range(1, len(nums)):
            dp.append(1)
            for j in range(len(dp)-1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


if __name__ == "__main__":
    s = Solution()
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [0, 8, 4, 12, 2]  # 3
    print(s.lengthOfLIS(nums))  # 4
