# coding: utf-8
''' 238. 除自身以外数组的乘积

给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：(未实现)
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
'''


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        left = [1] * len(nums)
        right = [1] * len(nums)
        output = [0] * len(nums)
        i = 1
        while i <= len(nums) - 1:
            left[i] = left[i - 1] * nums[i - 1]
            right[-(i + 1)] = right[-i] * nums[-i]
            i += 1
        # 注意这里 right 应该要反转，不做 reverse 处理就注意对称
        for index in range(len(nums)):
            output[index] = left[index] * right[index]
        return output


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    print(s.productExceptSelf(nums))
