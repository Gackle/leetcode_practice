# -*- coding: utf-8 -*-
""" 55. 跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

思路：贪心算法
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1      # 目标 index ，为数组长度-1（从 0 开始）
        max_location = 0            # 当前最大可达 index
        location = 0                # 当前 index
        while location <= max_location:     # 当前 index 并未超过最大可达 index
            # 计算当前 index 的最大可达 index ，更新最大可达 index
            max_location = max(max_location, location + nums[location])
            # 如果最大可达 index 大于等于目标 index ，退出
            if max_location >= target:
                return True
            # 当前 index 不符合要求，尝试往前走一步
            location += 1
        # 当前 index 达到了最大可达 index 且最大可达 index 不等于目标 index
        return False


class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    nums = [2, 0]   # True
    # nums = [2, 3, 1, 1, 4]  # True
    # nums = [3, 2, 1, 0, 4]  # False
    # nums = [2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8,
    #         0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6]
    print(s.canJump(nums))
