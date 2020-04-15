# -*- coding: utf-8 -*-
""" 542. 01矩阵
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。

示例 1:
输入:
0 0 0
0 1 0
0 0 0
输出:
0 0 0
0 1 0
0 0 0

示例 2:
输入:
0 0 0
0 1 0
1 1 1
输出:
0 0 0
0 1 0
1 2 1

提示：
BFS DFS
"""
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        out = [[-1] * n for _ in range(m)]
        queue = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    out[i][j] = 0
                    queue.append((i, j, 0))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            point = queue.pop(0)
            for d in directions:
                i = point[0] + d[0]
                j = point[1] + d[1]
                if i < 0 or i >= m or j < 0 or j >= n:
                    continue
                if out[i][j] == -1:
                    dist = point[2] + 1
                    out[i][j] = dist
                    queue.append((i, j, dist))
        return out


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]
    matrix = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    print(s.updateMatrix(matrix))
