# coding: utf-8
""" 213. 打家劫舍 II

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例：
    输入: [2,3,2]
    输出: 3
    解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

思路:
    money[i] = max(money[i-1], money[i-2] + nums[i])
"""


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        # 计算第一个房子不算最后一个房子
        sum1 = self.rob_recursion(0, n - 1, nums)
        # 不算第一个房子计算最后一个房子
        sum2 = self.rob_recursion(1, n, nums)
        return max(sum1, sum2)

    def rob_recursion(self, start, end, nums):
        pre = 0
        pre_pre = 0
        for i in range(start, end):
            if pre_pre + nums[i] >= pre:
                pre_pre, pre = pre, pre_pre + nums[i]
            else:
                pre_pre = pre
        return pre


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 2]
    print(s.rob(nums))
