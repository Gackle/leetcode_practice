# coding: utf-8
''' 136. 只出现一次的数字
'''


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or nums == []:
            return nums
        return_value = 0
        for num in nums:
            return_value ^= num
        return return_value


if __name__ == '__main__':
    s = Solution()
    nums = [4, 1, 2, 1, 2]
    nums = [-1, 2, 3, 0, 3, 0, 2]
    print(s.singleNumber(nums))
