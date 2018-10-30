# coding: utf-8
""" 179. 最大数
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:
输入: [10,2]
输出: 210

示例 2:
输入: [3,30,34,5,9]
输出: 9534330

思路：非常巧妙地思路，如何对比两个位数不同的数字如何合并得到最大 ——
直接合并一下比较大小就好了
"""


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ""
        result = [nums[0]]
        for num in nums[1:]:
            i = 0
            while i < len(result):
                a = int(str(num) + str(result[i]))
                b = int(str(result[i]) + str(num))
                if a >= b:
                    result.insert(i, num)
                    break
                else:
                    i += 1
            if i == len(result):
                result.append(num)
        s = ""
        for i in result:
            if i == 0 and s == "0":
                continue
            s += str(i)
        return s

if __name__ == '__main__':
    s = Solution()
    nums = [0, 0]
    print(s.largestNumber(nums))
