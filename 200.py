# coding: utf-8
''' 200. 岛屿的个数

给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
'''


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    count += 1
                    self.find(row, column, grid)
        return count

    def find(self, row, column, grid):
        '''
        :type row: int
        :type column: int
        :type grid: List[List[str]]
        '''
        grid[row][column] = "-1"
        if row > 0 and grid[row - 1][column] == "1":
            self.find(row - 1, column, grid)
        if column > 0 and grid[row][column - 1] == "1":
            self.find(row, column - 1, grid)
        if row < len(grid) - 1 and grid[row + 1][column] == "1":
            self.find(row + 1, column, grid)
        if column < len(grid[0]) - 1 and grid[row][column + 1] == "1":
            self.find(row, column + 1, grid)


class Solution2:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == [[]] or grid is None or grid == []:
            return 0
        self.count = 0
        # 以列表来表示并查集中的树
        self.union_set = [i for i in range(len(grid[0]) * len(grid))]
        for i in range(len(self.union_set)):
            row = i // len(grid[0])
            column = i % len(grid[0])
            if grid[row][column] == "1":
                self.count += 1

        for j in range(len(self.union_set)):
            row = j // len(grid[0])
            column = j % len(grid[0])
            down = row + 1
            right = column + 1
            if down < len(grid) and grid[row][column] == "1" and grid[down][column] == "1":
                self.union(j, j + len(grid[0]))
            if right < len(grid[0]) and grid[row][column] == "1" and grid[row][right] == "1":
                self.union(j, j + 1)

        return self.count

    def union(self, m, n):
        root_of_m = self.find(m)
        root_of_n = self.find(n)
        if root_of_m != root_of_n:
            # 这里隐含了一个条件：如果 m 的父节点和 n 的父节点不相等，一定会有 root_of_m 小于 root_of_n，同时 root_of_m 的子数目会更多
            self.union_set[root_of_n] = root_of_m
            self.count -= 1

    def find(self, child):
        parent = child
        while parent != self.union_set[parent]:
            self.union_set[parent] = self.union_set[self.union_set[parent]]
            parent = self.union_set[parent]
        return parent


if __name__ == '__main__':
    s = Solution2()
    grid = [
        ["1", "1", "1", "1", 0],
        ["1", "1", 0, "1", 0],
        ["1", "1", 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    # grid = [
    #     ["1", "1", 0, 0, 0],
    #     ["1", "1", 0, 0, 0],
    #     [0, 0, "1", 0, 0],
    #     [0, 0, 0, "1", "1"]
    # ]
    # grid = [
    #     ["1"]
    # ]
    print(s.numIslands(grid))
