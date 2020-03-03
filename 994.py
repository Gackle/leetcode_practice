# coding: utf-8
""" 994. 腐烂的橘子
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

提示：广度优先 BFS
"""
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n < 1:
            return -1

        queue = []
        queue = []
        minute = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    be_infected = self._infected(i, j, n, m, grid)
                    queue.extend(be_infected)

        while queue:
            minute += 1
            count = 0
            for orange in queue:
                count += 1
                grid[orange[0]][orange[1]] = 2
            for i in range(count):
                orange = queue.pop(0)
                be_infected = self._infected(orange[0], orange[1], n, m, grid)
                queue.extend(be_infected)
        else:
            return -1 if self._check_health(n, m, grid) else minute

    def _infected(self, x, y, n, m, grid):
        """ 返回该橘子周围待感染橘子
        """
        result = []
        direction = ((1, 0), (-1, 0), (0, -1), (0, 1))
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 判断点越界
                continue
            if grid[nx][ny] == 1:
                result.append((nx, ny))
        return result

    def _check_health(self, n, m, grid):
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return True
        return False


class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n < 1:
            return -1

        queue1 = []
        queue2 = []
        minute = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    be_infected = self._infected(i, j, n, m, grid)
                    queue1.extend(be_infected)

        while self._check_health(n, m, grid):
            if len(queue1) == 0:
                # 没有新增感染
                return -1
            minute += 1
            queue2 = queue1.copy()
            queue1.clear()
            for orange in queue2:
                grid[orange[0]][orange[1]] = 2
                be_infected = self._infected(orange[0], orange[1], n, m, grid)
                queue1.extend(be_infected)
        else:
            return minute

    def _infected(self, x, y, n, m, grid):
        """ 返回该橘子周围待感染橘子
        """
        result = []
        direction = ((1, 0), (-1, 0), (0, -1), (0, 1))
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 判断点越界
                continue
            if grid[nx][ny] == 1:
                result.append((nx, ny))
        return result

    def _check_health(self, n, m, grid):
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return True
        return False


class Solution3:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        import collections
        R, C = len(grid), len(grid[0])
        queque = collections.deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    queque.append((r, c, 0))

        def nextoranges(r, c):
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        d = 0
        while queque:
            r, c, d = queque.popleft()
            for nr, nc in nextoranges(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queque.append((nr, nc, d+1))
        if any(1 in row for row in grid):
            return -1
        return d


if __name__ == "__main__":
    s = Solution3()
    # grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]  # 4
    # grid = [[1]]  # -1
    # grid = [[0, 2]]  # 0
    # grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]  # -1
    # grid = [[0, 1]]  # -1
    grid = [[2, 2], [1, 1], [0, 0], [2, 0]]  # 1
    print(s.orangesRotting(grid))
