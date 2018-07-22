# coding: utf-8
''' 41. 缺失的第一个正数

算法的时间复杂度应为O(n)，并且只能使用常数级别的空间
'''


class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        res = 1
        if n == 0:
            return res
        for num in range(0, n):
            if nums[num] < 0:
                nums[num] = 0
            if nums[num] > n:
                nums[num] = 0
        flag = -(n + 1)

        for num in nums:
            if num != 0 and num != flag:
                if nums[abs(num) - 1] == 0:
                    nums[abs(num) - 1] = flag
                elif nums[abs(num) - 1] > 0:
                    nums[abs(num) - 1] *= -1

        while res <= n and nums[res - 1] < 0:
            res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([3, 4, -1, 1]))
