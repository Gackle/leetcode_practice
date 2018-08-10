# coding: utf-8
"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

思路：直接找到和边界的点相联通的点并标记为其他节点，其余的 O 节点就可以直接置换为 X
"""


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == [] or board == [[]]:
            return
        width = len(board[0])
        height = len(board)

        # 对四条边进行 dfs
        i = 0
        while i < width:
            if board[0][i] == "O":
                self.combine_node(0, i, width, height, board)
            if board[height - 1][i] == "O":
                self.combine_node(height - 1, i, width, height, board)
            i += 1

        j = 0
        while j < height:
            if board[j][0] == "O":
                self.combine_node(j, 0, width, height, board)
            if board[j][width - 1] == "O":
                self.combine_node(j, width - 1, width, height, board)
            j += 1

        # 还原图
        row = 0
        while row < height:
            column = 0
            while column < width:
                if board[row][column] == "O":
                    board[row][column] = "X"
                elif board[row][column] == "/":
                    board[row][column] = "O"
                column += 1
            row += 1

    def combine_node(self, row, column, width, height, board):
        """
        :type row: int
        :type column: int
        :type width: int
        :type height: int
        :type board: List[List[str]]
        dfs
        """
        board[row][column] = "/"
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in directions:
            nrow = row + direction[0]
            ncolumn = column + direction[1]
            if nrow < 0 or nrow >= height or ncolumn < 0 or ncolumn >= width:
                continue
            if board[nrow][ncolumn] == "O":
                self.combine_node(nrow, ncolumn, width, height, board)


if __name__ == '__main__':
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    board = []
    s = Solution()
    s.solve(board)
