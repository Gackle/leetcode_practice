# coding: utf-8
""" 26. 删除排序数组中的重复项
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        i = 0
        while len(nums) > i + 1:
            if nums[i] == nums[i+1]:
                j = i
                while j < len(nums) and nums[j] == nums[i]:
                    j += 1
                else:
                    nums[i:j] = [nums[i]]
            i += 1
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 2, 2, 3, 4, 5, 6, 6, 6]
    nums = [1, 1, 2]
    print(s.removeDuplicates(nums))
