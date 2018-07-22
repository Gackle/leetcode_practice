# coding: utf-8
''' 153. 寻找旋转排序数组中的最小值

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。
'''


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == [] and nums is None:
            return nums
        left, right = 0, len(nums) - 1
        while left < right and nums[left] > nums[right]:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 4, 5, 1, 2]
    print(s.findMin(nums))
