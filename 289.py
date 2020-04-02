# -*- coding: utf-8 -*-
""" 289. 生命游戏
根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），
或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

1. 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
2. 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
3. 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
4. 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。

输入：
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出：
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

要点：纯搬砖，关键是使用符合状态可以减少空间开销，对于原先是死的变活了的，状态为 2 ，
对于原先是活的后面死了状态为 -1 ，不变的保持不变（1或者0），
第一次遍历数组设置状态，第二次“一次性”修改状态
"""
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1),
                     (-1, -1), (1, 1), (1, -1)]  # 八方旅人
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                cell = board[row][col]
                live_cells = 0
                # 遍历邻居
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]
                    if r < 0 or r >= rows or c < 0 or c >= cols:
                        continue
                    live_cells += 1 if board[r][c] == 1 or board[r][c] == -1 else 0
                # 规则 1 & 3
                if cell and (live_cells < 2 or live_cells > 3):
                    board[row][col] = -1
                # 规则 4
                if not cell and live_cells == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0

        print(board)


if __name__ == "__main__":
    s = Solution()
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    s.gameOfLife(board)
    # print(board)
