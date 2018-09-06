# coding: utf-8
""" 53. 最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

    输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        if nums == []:
            return None
        i = 0
        max_count = -sys.maxsize - 1
        current = 0
        while i < len(nums):
            current = max(current + nums[i], nums[i])
            max_count = max(max_count, current)
            i += 1
        return max_count

if __name__ == '__main__':
    s = Solution()
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [1, 2]
    print(s.maxSubArray(nums))