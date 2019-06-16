# coding: utf-8
""" 1091. 二进制矩阵中的最短路径

在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。
一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：

- 相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
- C_1 位于 (0, 0)（即，值为 grid[0][0]）
- C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
- 如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）

返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。

思路：
广度优先 - 最后超时 。。。。
"""


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1
        if grid[0][0] != 0:
            return -1
        self.n = len(grid)  # height
        length = self.n**2
        # 上下左右，左上，右上，左下，右下
        self.direction = [(-1, 0), (1, 0), (0, -1), (0, 1),
                          (-1, -1), (-1, 1), (1, -1), (1, 1)]
        visited = "1" + "0" * (length-1)
        min_step = False
        already_step = 0
        # 广度遍历
        queue = [(0, 0, visited, already_step)]
        while queue:
            point = queue.pop(0)
            a = point[0]
            b = point[1]
            visited = point[2]
            astep = point[3]
            if a == self.n-1 and b == self.n-1:
                min_step = astep + 1
                break
            for d in self.direction:
                na = a + d[0]
                nb = b + d[1]
                if self.can_visit(na, nb, visited) and grid[na][nb] != 1:
                    next_point = na*self.n+nb
                    next_visited = visited[:next_point] + \
                        "1" + visited[next_point+1:]
                    queue.append((na, nb, next_visited, astep+1))
                else:
                    continue
        return -1 if not min_step else min_step

    def can_visit(self, na, nb, visited):
        if na not in range(self.n) or nb not in range(self.n) or visited[(na)*self.n+(nb)] == '1':
            return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    # grid = [
    #     [0, 1],
    #     [1, 0],
    # ]
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(s.shortestPathBinaryMatrix(grid))
