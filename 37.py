# coding: utf-8
''' 37. 解数独

编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
'''


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board, 0, 0)
        print(board)

    def dfs(self, board, rid, cid):
        '''
        :type board: List[List[str]]
        :type rid: int
        :type cid: int

        深度遍历
        '''
        if cid >= 9:
            return self.dfs(board, rid + 1, 0)
        elif rid >= 9:
            # 遍历完成
            return True
        elif board[rid][cid] != '.':
            return self.dfs(board, rid, cid + 1)
        else:
            for value in range(1, 10):
                if self.isValid(board, value, rid, cid):
                    if self.dfs(board, rid, cid + 1):
                        return True
                board[rid][cid] = '.'
        return False

    def isValid(self, board, value, rid, cid):
        '''
        :type board: List[List[str]]
        :type value: int
        :type rid: int
        :type cid: int
        '''
        # 判断行重复
        if str(value) in board[rid]:
            return False
        # 判断列重复
        if str(value) in [[x[cid] for x in board] for cid in [cid]][0]:
            return False
        # 判断九宫格
        row_group = rid // 3
        column_group = cid // 3
        for i in range(3):
            group_row = [board[row_group * 3 + i][column_group * 3],
                         board[row_group * 3 + i][column_group * 3 + 1],
                         board[row_group * 3 + i][column_group * 3 + 2]]
            if str(value) in group_row:
                return False
        board[rid][cid] = str(value)
        return True


if __name__ == '__main__':
    board = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '.']]
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    board = [['.', '.', '7', '9', '.', '.', '.', '.', '8'],
             ['.', '.', '.', '3', '6', '.', '.', '5', '.'],
             ['5', '9', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '6', '.', '.', '.', '2', '.', '5'],
             ['4', '.', '.', '.', '5', '3', '.', '1', '.'],
             ['.', '.', '.', '6', '.', '8', '.', '.', '.'],
             ['.', '.', '9', '.', '.', '.', '.', '.', '7'],
             ['.', '3', '.', '.', '4', '.', '.', '.', '.'],
             ['.', '.', '2', '.', '.', '1', '3', '.', '.']]
    s = Solution()
    # print(s.solveSudoku(board))
    s.solveSudoku(board)
