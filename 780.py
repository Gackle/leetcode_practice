# coding: utf-8
""" 780. 到达终点
从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。
给定一个起点 (sx, sy) 和一个终点 (tx, ty)，如果通过一系列的转换可以从起点到达终点，则返回 True ，否则返回 False。

示例:
输入: sx = 1, sy = 1, tx = 3, ty = 5
输出: True
解释:
可以通过以下一系列转换从起点转换到终点：
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

输入: sx = 1, sy = 1, tx = 2, ty = 2
输出: False

输入: sx = 1, sy = 1, tx = 1, ty = 1
输出: True

注意:
sx, sy, tx, ty 是范围在 [1, 10^9] 的整数。

思路：（数学题不好都是抄别人的）从 (sx, sy) 开始会有很多种可能，但是从 (tx, ty) 倒退则只有一种可能 
==> 注意，每个 (tx, ty) 中大数的组合都可以拆分为两个小数，同时可以发现 (tx, ty) 都是单调递增的
==> 做法：不停的往前推演，如果推演结果中得到 tx'<sx 或 ty'<sy ，则可以输出 False 了
==> 优化：速度太慢，无论是递归还是循环！因此不能单纯的递减（即 tx = tx-ty 或 ty = ty-tx），
我们可以发现，实际上对于大数，会存在：大数 = 原数+k*小数，因此求大数的原数，其实就是求大数对小数的余数。这样就能加速很多了
"""


class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            elif tx < ty:
                ty %= tx
            else:
                return False
        if tx == sx:
            return (ty-sy) % sx == 0
        elif ty == sy:
            return (tx-sx) % sy == 0
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    sx, sy, tx, ty = 1, 5, 2, 8
    print(s.reachingPoints(sx, sy, tx, ty))
