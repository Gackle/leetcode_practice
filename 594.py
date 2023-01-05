# coding: utf-8
""" 594. 最长和谐子序列
和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。
现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。
数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。

示例 1：
输入：nums = [1,3,2,2,5,2,3,7]
输出：5
解释：最长的和谐子序列是 [3,2,2,2,3]

示例 2：
输入：nums = [1,2,3,4]
输出：2

示例 3：
输入：nums = [1,1,1,1]
输出：0

提示：
1 <= nums.length <= 2 * 10^4
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        items = {}
        for i in nums:
            count = items.get(i, None)
            if count is None:
                items[i] = 1
            else:
                items[i] = count + 1
        result = 0
        keys = sorted(items.keys())
        for key in keys:
            if (key + 1) in keys:
                result = max(result, items[key] + items[key + 1])
        return result


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4]
    assert s.findLHS(nums=nums) == 2, f"2 != findLHS({nums})"
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    assert s.findLHS(nums=nums) == 5, f"5 != findLHS({nums})"
    nums = [1, 1, 1, 1]
    assert s.findLHS(nums=nums) == 0, f"0 != findLHS({nums})"
