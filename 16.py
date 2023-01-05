# coding: utf-8
""" 16. 最接近的三数和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 
提示：
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

思路：排序，然后双指针，时间复杂度为 O(n^2)
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """ 要得到三个数 abc 使得 a+b+c 的和最接近 target
        """
        closed = float('inf')

        def update_closed(cur):
            # 更新最接近点
            nonlocal closed
            if abs(cur-target) < abs(closed-target):
                closed = cur

        # 关键key：排序，只有排序了双指针才有意义
        nums.sort()

        i = 0
        # 遍历数组作为 a
        while i < len(nums) - 1:
            rest = target - nums[i]
            left = i + 1
            right = len(nums) - 1
            # 双指针分别指向 b 和 c
            while left < right:
                sum_bc = nums[left] + nums[right]
                # a+b+c == target 直接返回
                if sum_bc == rest:
                    return target
                # 更新最接近点
                update_closed(sum_bc + nums[i])
                # b + c < target - a ， 增大 b
                if sum_bc < rest:
                    left += 1
                else:
                    # b + c > target - a ， 减少 c
                    right -= 1
            i += 1
        return closed


if __name__ == "__main__":
    s = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    assert s.threeSumClosest(
        nums, target) == 2, f"case 1 {s.threeSumClosest(nums, target)} neq 2"
