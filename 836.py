# coding: utf-8
""" 836. 矩形重叠
矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
给出两个矩形，判断它们是否重叠并返回结果。
"""
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2
        if b1 >= y2 or a1 >= x2 or b2 <= y1 or a2 <= x1:
            return False
        return True


if __name__ == "__main__":
    s = Solution()
    rec1 = [0, 0, 1, 1]
    rec2 = [1, 0, 2, 1]
    print(s.isRectangleOverlap(rec1, rec2))
