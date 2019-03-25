# coding: utf-8
""" 228. 汇总区间
给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。

示例 1:
输入: [0,1,2,4,5,7]
输出: ["0->2","4->5","7"]
解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。

示例 2:
输入: [0,2,3,4,6,8,9]
输出: ["0","2->4","6","8->9"]
解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums
        return_data = []
        start = nums[0]
        cur = start
        for i in nums[1:]:
            if i == cur + 1:
                cur = i
            else:
                if cur != start:
                    # 区间不止一个元素
                    return_data.append("%d->%d" % (start, cur))
                else:
                    return_data.append(str(start))
                start = i
                cur = start
        # 尾元素处理
        if cur != start:
            return_data.append("%d->%d" % (start, cur))
        else:
            return_data.append(str(start))
        return return_data


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 2, 4, 5, 7]
    # nums = [0, 2, 3, 4, 6, 8, 9]
    print(s.summaryRanges(nums))
