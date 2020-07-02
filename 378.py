# coding: utf-8
"""378. 有序矩阵中第K小的元素
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

示例：
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。

提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。
"""
from typing import List


class Solution:
    # 矩阵的二分查找
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            # 二分路线
            while i > 0 and j < n:
                if matrix[i][j] <= mid:
                    # 将当前所在列不大于 mid 的数量（即 i+1）累加到答案中，并向右移动
                    num += i + 1
                    j += 1
                else:
                    # 否则向上移动（相当于缩小了矩阵）
                    i -= 1
            # 要找到第 K 个大的数，按照二分法的思路，对有序数组进行二分，直到left 的长度为 K -1，则 right 的元素即为 K 大小的值
            return num >= k

        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                # 二分查找
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    r = s.kthSmallest(matrix, k)
    assert r == 13, f"case 1 {r} neq 13"
