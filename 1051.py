# coding: utf-8
""" 1051. 高度检查器
拍年度纪念照时，要求学生按照高度非递减的顺序排列。
返回没有站在正确位置的最小学生人数。（该人数是能让所有学生以不递减高度排列的必要移动人数。）

示例：
输入：[1,1,4,2,1,3]
输出：3
解释：
高度为 4、3 和最后一个 1 的学生没有站在正确的位置。

提示：
1 <= heights.length <= 100
1 <= heights[i] <= 100

思路：
排序后对比，如果站错了位置，那么对应正确的顺序其位置就不对了
"""


class Solution:
    def heightChecker(self, heights) -> int:
        correct = sorted(heights)
        n = len(heights)
        count = 0
        for i in range(n):
            if correct[i] != heights[i]:
                count += 1
        return count

if __name__ == "__main__":
    s = Solution()
    # l = [1, 1, 4, 2, 1, 3]
    l = [2, 1, 2, 1, 1, 2, 2, 1]
    print(s.heightChecker(l))
