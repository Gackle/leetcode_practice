# coding: utf-8
""" 42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

思路：先找到柱状图的最高点，然后分别从最左、最右往最高点靠拢，遇到比当前节点低的就计算水位
遇到比它高的就做节点转移，同时要记得计算最高点之间的水位（不止一个最高点），空间复杂度为常数，时间复杂度为 O(n)
P.S. 这道题思路明确之后，写下来超快...而且一次 AC ... 爽
"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        # 先遍历柱状图的最高点（不止一个）
        max_h = [(0, -1)]
        for i, h in enumerate(height):
            if h > max_h[0][0]:
                max_h = [(h, i)]
            elif h == max_h[0][0]:
                max_h.append((h, i))
        # 分别从左右两边遍历到最高点，边遍历边计算雨水面积
        water = 0
        # 左遍历
        left = 0
        while left < max_h[0][1]:
            if height[left] == 0:
                left += 1
                continue
            right = left + 1
            while right <= max_h[0][1]:
                if height[right] < height[left]:
                    water += height[left] - height[right]
                    right += 1
                else:
                    left = right
                    break
        # 右遍历
        right = len(height) - 1
        while right > max_h[-1][1]:
            left = right - 1
            while left >= max_h[-1][1]:
                if height[left] < height[right]:
                    water += height[right] - height[left]
                    left -= 1
                else:
                    right = left
                    break
        # 计算最高点之间的水位差
        rest = 0
        if len(max_h) > 1:
            rest += (max_h[-1][1] - max_h[0][1] + 1) * height[max_h[0][1]] - sum(height[max_h[0][1]:max_h[-1][1]+1])
        return water + rest


if __name__ == '__main__':
    s = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap(height))
