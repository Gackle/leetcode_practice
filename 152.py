# coding: utf-8
''' 152. 乘积最大子序列

给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

这道题的关键点在于，因为存在负数元素，因此同时要记录序列的最小值，一旦乘以负数有可能最小值变最大值

这道题没有严格按照动态规划的思想去做，因为动态规划在我的理解中它是可以追溯的，可以直到每一个位置开始的子序列的最大最小值，这才是关键

'''


class Solution:
    ''' 最速解法
    '''

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCache = [0 for i in range(len(nums))]
        minCache = [0 for i in range(len(nums))]

        minCache[0] = maxCache[0] = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            minCache[i] = maxCache[i] = nums[i]
            if nums[i] > 0:
                maxCache[i] = max(maxCache[i], maxCache[i - 1] * nums[i])
                minCache[i] = min(minCache[i], minCache[i - 1] * nums[i])
            elif nums[i] < 0:
                maxCache[i] = max(maxCache[i], minCache[i - 1] * nums[i])
                minCache[i] = min(minCache[i], maxCache[i - 1] * nums[i])

            result = max(result, maxCache[i])

        return result


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, -2, 4]
    print(s.maxProduct(nums))
