# coding: utf-8
''' 462. 最少移动次数使数组元素相等 II

给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。
'''


class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid_num = nums[len(nums) // 2]
        total_moves = 0
        for i in nums:
            total_moves += abs(i - mid_num)
        return total_moves


if __name__ == '__main__':
    s = Solution()
    nums = [8, 3, 1, 2, 3, 0, 9]
    print(s.minMoves2(nums))
