# coding: utf-8
""" 324. 摆动排序 II

给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？

"""


class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        for i in range(1, n, 2):
            tail = nums.pop()
            nums.insert(i, tail)
        tail = n - 1 if n & 1 else n - 2
        for j in range(0, ((n + 1) // 2), 2):
            nums[j], nums[tail] = nums[tail], nums[j]
            tail -= 2
        print(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 1, 1, 6, 4]
    nums = [1, 5, 1, 1, 6]
    nums = [1, 3, 2, 2, 3, 1]
    # nums = [1, 1, 2, 2, 3, 3]
    print(s.wiggleSort(nums))
