# coding: utf-8
""" 169. 求众数
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3

示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2

思路：哈希表 dict 的时间复杂度为 O(n) 其实也可以接受，空间复杂度会稍大，
其他诸如分治也差不多时间，实际上算上堆栈开销空间复杂度其实也相差无几
排序法的思路是：先排序再取中间值（出现次数超过一半的元素必定是数组中的中间元素），排序算法有快有慢，快的话 O(NlogN)，空间复杂度 O(1)

这里提到了一种 **摩尔投票法 Moore Voting** —— 需要 O(n) 的时间复杂度和 O(1) 的空间复杂度：
- 先将第一个数字假设为众数，然后把计数器设为1，比较下一个数和此数是否相等，
- 若相等则计数器加一，反之减一。
- 然后看此时计数器的值，若为零，则将下一个值设为候选众数。
- 以此类推直到遍历完整个数组，当前候选众数即为该数组的众数。
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        current = nums[0]
        for num in nums[1:]:
            if current == num:
                count += 1
            else:
                if count == 0:
                    current = num
                    count = 1
                else:
                    count -= 1
        return current


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(s.majorityElement(nums))
