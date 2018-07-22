# coding: utf-8
''' 137. 只出现一次的数字 II

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
'''


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0
        if nums is None or nums == []:
            return nums
        return_value = 0
        for i in range(32):
            sum = 0
            for num in nums:
                if num < 0:
                    flag += 1
                    num = -num
                sum += (num >> i & 1)
            return_value |= (sum % 3) << i
        return -return_value if flag % 3 else return_value

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = sum(set(nums)) * 3 - sum(nums)
        return int(num / 2)


if __name__ == '__main__':
    s = Solution()
    # nums = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
    nums = [2, 2, 3, 2]
    print(s.singleNumber(nums))
