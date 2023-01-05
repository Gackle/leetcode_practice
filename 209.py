# coding: utf-8
""" 209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

思路：双指针 二分查找
"""
from typing import List
import bisect


class Solution:
    # 前缀和 + 二分查找
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans


class Solution1():
    # 双指针（滑动窗口）
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans


if __name__ == "__main__":
    S = Solution()
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    r = S.minSubArrayLen(s, nums)
    assert r == 2, f"case 1: {r} neq 2"
    s = 100
    nums = []
    r = S.minSubArrayLen(s, nums)
    assert r == 0, f"case 2: {r} neq 0"
    s = 11
    nums = [1, 2, 3, 4, 5]
    r = S.minSubArrayLen(s, nums)
    assert r == 3, f"case 3: {r} neq 3"
