# coding: utf-8
""" 628. 三个数的最大乘积

给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
注意:

给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
"""


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            return reduce(lambda a, b: a * b, nums)
        neg_num = 0
        neg_list = [0, 0]
        pos_list = [0, 0, 0]
        for num in nums:
            if num < 0:
                if num < neg_list[0]:
                    neg_list.pop()
                    neg_list.insert(0, num)
                elif num < neg_list[1]:
                    neg_list[1] = num
                neg_num += 1
            elif num > 0:
                if num > pos_list[0]:
                    pos_list.pop()
                    pos_list.insert(0, num)
                elif num > pos_list[1]:
                    pos_list.pop()
                    pos_list.insert(1, num)
                elif num > pos_list[2]:
                    pos_list[2] = num

        if neg_num >= 2:
            return max(neg_list[0] * neg_list[1] * pos_list[0], reduce(lambda a, b: a*b, pos_list))
        else:
            return reduce(lambda a, b: a*b, pos_list)


if __name__ == '__main__':
    s = Solution()
    nums = [-710,-107,-851,657,-14,-859,278,-182,-749,718,-640,127,-930,-462,694,969,143,309,904,-651,160,451,-159,-316,844,-60,611,-169,-73,721,-902,338,-20,-890,-819,-644,107,404,150,-219,459,-324,-385,-118,-307,993,202,-147,62,-94,-976,-329,689,870,532,-686,371,-850,-186,87,878,989,-822,-350,-948,-412,161,-88,-509,836,-207,-60,771,516,-287,-366,-512,509,904,-459,683,-563,-766,-837,-333,93,893,303,908,532,-206,990,280,826,-13,115,-732,525,-939,-787]
    print(s.maximumProduct(nums))
