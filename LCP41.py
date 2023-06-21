# encoding: utf-8
""" LCP41. 黑白棋反转
在 n*m 大小的棋盘中，有黑白两种棋子，黑棋记作字母 "X", 白棋记作字母 "O"，空余位置记作 "."
将提供给选手一个未形成可翻转棋子的棋盘残局，其状态记作 chessboard。若下一步可放置一枚黑棋，请问选手最多能翻转多少枚白棋。
广度优先搜索 数组 矩阵
"""
from typing import List
class Solution:
    """我们可以用「广度优先搜索」来解决这个问题，我们对每一个空余位置尝试黑棋放置，
    用一个队列来存储正在进行「翻转操作」的黑棋位置，若队列非空，我们从队列中取出队首元素，
    进行行、列和对角线 8 个方向判断是否有可以翻转的白棋——判断沿着方向是否是连续的一段白棋并以另一颗黑棋结尾。
    若有可以翻转的白棋，则将这些白旗进行翻转，并加入队列中。
    直至队列为空表示一次放置黑棋结束。
    """
    def flipChess(self, chessboard: List[str]) -> int:
        n, m = len(chessboard), len(chessboard[0])
        direction = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]  # 八个遍历方向(逆时针)
        res = 0

        def bfs(i, j) -> int:
            c = [[item for item in row] for row in chessboard]
            cur = 0
            queue = [(i, j)]
            while len(queue) > 0:
                x, y = queue.pop(0)
                for dx, dy in direction:
                    memcache = []
                    row, column = x + dx, y + dy
                    while 0 <= row < n and 0 <= column < m and c[row][column] == "O":
                        memcache.append((row, column))
                        row, column = row + dx, column + dy
                    if 0 <= row < n and 0 <= column < m and c[row][column] == "X": # 符合翻转条件
                        # 翻转
                        for px, py in memcache:
                            cur += 1
                            queue.append((px, py))
                            c[px][py] = "X"
            return cur


        for i in range(n):
            for j in range(m):
                if chessboard[i][j] == ".":
                    res = max(res, bfs(i, j))
    
        return res
  
if __name__ == '__main__':
    s = Solution()
    examples = [
        (["....X.","....X.","XOOO..","......","......"], 3),
        ([".X.",".O.","XO."], 2),
        ([".......",".......",".......","X......",".O.....","..O....","....OOX"], 4),
    ]
    for chessboard, ans in examples:
        res = s.flipChess(chessboard)
        assert res == ans, f"flipChess({chessboard}) except {ans} but got {res}"
    
    print("You Pass!")