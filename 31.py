# coding: utf-8
''' 31. 下一个排列

只能原地修改，并且使用常数量的空间
'''


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 1
        while index > 0:
            if nums[index] <= nums[index - 1]:
                index -= 1
            else:
                # 往后找，找到比 nums[index - 1] 大的最小数
                mini = index
                rindex = index + 1
                while rindex < len(nums):
                    if nums[rindex] > nums[index - 1] and nums[rindex] <= nums[mini]:
                        mini = rindex
                    rindex += 1
                nums[index - 1], nums[mini] = nums[mini], nums[index - 1]
                # 对 index 位置开始往后的子排列按从小到大排序: 这里用选择排序
                while index < len(nums):
                    jindex = index + 1
                    while jindex < len(nums):
                        if nums[index] > nums[jindex]:
                            nums[index], nums[jindex] = nums[jindex], nums[index]
                        jindex += 1
                    index += 1
                break

        if index == 0:
            nums.reverse()

        print(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5]
    s.nextPermutation(nums)
