# coding: utf-8
"""
华容道 —— (回溯)
有1到8八个数字，放在一个3x3的九宫格里面，那么会留下一个空格。

|3|4|1|
-------
|5|6| |
-------
|8|2|7|

空格可以和上下左右的数字进行交换，你可以认为空格在移动。如果移动成

|1|2|3|
-------
|4|5|6|
-------
|7|8| |

则游戏胜利。
你需要完成以下2件事情：
1、给出数据结构来描述这个过程。
2、给你一个初始状态，告诉我能不能胜利，并给出如何移动才能胜利。
"""


class Solution(object):
    def __init__(self):
        # 方向
        self.directions = [(1, 0),  # down
                           (-1, 0),  # up
                           (0, 1),  # right
                           (0, -1)  # left
                           ]
        # 步骤
        self.step = []
        # 目标状态
        self.target = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        # 起始状态
        self.status = []
        # [bfs]队列
        self.queue = []

    def huarongdao(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # 记录 matrix
        self.matrix = matrix
        # 记录起始位置
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == 0:
                    start = (i, j)
        # 记录起始状态(矩阵扁平化)
        self.status = sum(matrix, [])

        # DFS
        for direction in self.directions:
            if self.dfs(direction, start):
                return True
        return False

    def dfs(self, direction, current):
        """
        :type direction: Tuple[int, int]
        :param direction: 下一步的方向
        :type current: Tuple[int, int]
        :param current: 目前空格 0 的位置
        :rtype: bool
        """
        # 尝试移动
        n = (current[0] + direction[0], current[1] + direction[1])
        if not self.swap(current, n):
            return False
        # 记录步骤
        self.step.append(direction)
        # 记录状态(矩阵扁平化)
        status = sum(self.matrix, [])
        # 如果回到起始状态，剪枝
        if status == self.status:
            self.swap(n, current)
            self.step.pop()
            return False
        # 如果达到 target 状态，返回
        if status == self.target:
            return True

        # 都没有达到，继续下一个方向的深度搜索
        for next_step in self.directions:
            if self.dfs(next_step, n):
                return True

        # 都遍历完无法再往下走
        self.swap(n, current)
        self.step.pop()
        return False

    def swap(self, current_bit, next_bit):
        # 越界判断
        if not(0 <= next_bit[0] < 3) or not(0 <= next_bit[1] < 3):
            return False
        # 实际移动
        self.matrix[current_bit[0]][current_bit[1]
                                    ] = self.matrix[next_bit[0]][next_bit[1]]
        self.matrix[next_bit[0]][next_bit[1]] = 0
        return True


class Solution2(object):
    def huarongdao(self):
        pass

if __name__ == "__main__":
    s = Solution()
    # matrix = [
    #     [3, 4, 1],
    #     [5, 6, 0],
    #     [8, 2, 7]
    # ]
    matrix = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
    if s.huarongdao(matrix):
        print("Have Answer! the steps sequence is :")
        step_human = ["下" if x == (
            1, 0) else "上" if x == (-1, 0) else "右" if x == (0, 1) else "左" for x in s.step]
        for i in step_human:
            print(i, end="  ")
    else:
        print("No Answer!")
