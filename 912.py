# -*- coding: utf-8 -*-
""" 912. 排列数组
给你一个整数数组 nums，请你将该数组升序排列。
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length < 2:
            return nums
        left = nums[:length//2]
        right = nums[length//2:]
        return self.merge(self.sortArray(left), self.sortArray(right))

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        back = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                back.append(left[i])
                i += 1
            else:
                back.append(right[j])
                j += 1
        if i < len(left):
            back.extend(left[i:])
        if j < len(right):
            back.extend(right[j:])
        return back


if __name__ == "__main__":
    s = Solution()
    nums = [5, 1, 1, 2, 0, 0]
    nums = [5, 2, 3, 1]
    print(s.sortArray(nums))
