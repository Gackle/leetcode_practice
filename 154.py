# coding: utf-8
''' 154. 寻找旋转排序数组中的最小值 II

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。
'''


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == [] or nums is None:
            return None
        for index in range(1, len(nums)):
            if nums[index] < nums[index - 1]:
                return nums[index]
        return nums[0]


if __name__ == '__main__':
    s = Solution()
    nums = [4, 4, 5, 6, 7, 0, 1, 2]
    print(s.findMin(nums))
