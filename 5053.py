# coding: utf-8
""" 5053. 地图分析
你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。
我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
如果我们的地图上只有陆地或者海洋，请返回 -1。

示例 1：
|1|0|1|
|0|0|0|
|1|0|1|
输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释：
海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。

思路：
从某个海洋出发，寻找离他最近的陆地（广度遍历，又是广度遍历。。）
结果：
超时了。。。
"""


class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 处理全陆地和全海洋
        self.N = len(grid)
        a = sum([sum(i) for i in grid])
        if a == 0 or a == self.N * self.N:
            return -1
        max_distance = -1
        self.matrix = grid
        self.direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        for i in range(self.N):
            for j in range(self.N):
                if not grid[i][j]:  # 如果为海洋
                    distance = self.bfs((i, j))
                    max_distance = max(max_distance, distance)
        return max_distance

    def bfs(self, point):
        from sys import maxsize
        distance = maxsize
        queue = [point]
        out = []
        while queue:
            i, j = queue.pop()
            out.append((i, j))
            for x, y in self.direction:
                if i+x < 0 or i+x >= self.N or j+y < 0 or j+y >= self.N:
                    continue
                if not self.matrix[i+x][j+y] and (i+x, j+y) not in out:
                    queue.append((i+x, j+y))
                if self.matrix[i+x][j+y]:
                    # queue.clear()  # 找到了陆地，广度问题不再继续
                    distance = min(distance, abs(
                        x+i-point[0]) + abs(j+y-point[1]))
                    # break
        return distance


if __name__ == '__main__':
    s = Solution()
    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    grid = [
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 0, 0]
    ]
    grid = [[0,1,1,0,0,1,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,0,1,1,1,0,1,1,0,1,0,0,1,1],[0,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,1,1,0],[0,1,1,1,0,1,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1],[1,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1,1,0,1,0,1],[0,1,1,1,0,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0],[1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,0,0,1,1,1,0,0],[0,1,0,1,1,1,1,0,1,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,1,1,1,1,0,0,1,0,1,0,1,1,1,1,0,1,1,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1],[0,1,0,0,0,1,1,0,0,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0],[1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,0],[0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1],[1,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0],[1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,1,0,1,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0],[1,1,1,1,0,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1],[0,0,1,1,1,1,1,1,0,0,0,1,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,1,1,0],[1,0,1,0,0,0,1,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,0,1,1,1,1,0,0,1,0,1,0,1,0,1,1,0],[0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1],[0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,1,1,0,0,1,1,0,1,1,0,1,1,0,0,1,1],[0,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,0,0,1,1,0,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1],[1,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,1,0,1,1,0,0],[0,1,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,1,1,1,0,1,1,0,0,1,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,1,1,0,1,0,1,0,0,1,1],[1,0,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0,1,1,1,0,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,0,1,0,0,1,1,0,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,0,1,1],[1,1,1,1,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,1,1,0,1,1,1],[0,1,0,0,0,1,0,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,0,1,1,1,0,1,0,0,1],[0,1,0,1,0,1,1,1,0,1,0,0,0,0,1,0,0,1,0,1,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1],[0,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,1],[1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0],[0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0],[1,1,1,0,0,0,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,0,1,1,0,1,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0],[1,1,0,1,0,0,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,1,0,0,1,1,1,0,1,1,0,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1],[1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1],[0,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,0,0,1,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1],[0,1,0,1,1,0,0,1,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,0,1,1,1,0,1,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0],[0,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0],[0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,1],[0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1],[0,1,1,0,0,1,0,0,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1],[0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,1,1,1,1,0,1],[1,0,1,1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,0,0,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0],[1,1,1,0,0,1,0,1,1,0,1,1,1,0,1,0,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1],[1,0,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1],[1,0,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,0,1,1,0,0,0,0,1,1,0,1,0,1,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,0],[0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,1,1],[0,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,1,1,0],[1,1,1,0,0,0,1,1,0,1,1,1,1,0,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1],[1,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,0,0,0,0,1,1,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1,0,0,1,0,1,0,0,0,1,1,1],[1,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,1,1,1,0,0,1,0,1,0,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1],[1,1,0,1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0],[1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,1,1,0,0,0],[0,0,1,1,0,0,0,1,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0],[0,1,0,1,1,0,1,1,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,1,0,1,1,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,0,1],[1,0,1,0,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1],[1,0,0,1,1,1,1,0,1,1,1,0,1,0,0,1,0,1,1,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,1],[1,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,1],[1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,1,1,0,0,1,0,1,0,1,0,0,0,1,0],[0,0,1,1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,1,1,0,1],[1,1,1,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,1,0,1,1,0,0,1,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0],[0,0,1,1,0,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,1],[0,1,1,1,1,0,1,1,0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],[0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,0,0,1,0,0,0,1,0,0],[0,0,0,1,1,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0],[0,0,1,0,0,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,1,1,0,0,1,1,0,0,1,0,0,0,1,0,1],[1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,0,1,1,1,0,1,0,0,1,1,1,1,0,1,0,0,1,1,0,0,1,0,1,1,1,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,1],[0,1,0,1,0,1,1,0,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0],[0,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0],[0,1,1,0,0,1,0,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,0],[1,0,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1,1,1,1]]
    print(s.maxDistance(grid))
