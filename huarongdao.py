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
        self.directions = [(1, 1), (-1, -1), (-1, 1), (1, -1)]

    def huarongdao(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # 记录起始位置
        for i in range(3):
            for j in range(3):
                if matrix(i, j) == 0:
                    self.start = (i, j)

    def dfs(self, direction):
        """
        :type direction: Tuple(int, int)
        """
        pass


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [3, 4, 1],
        [5, 6, 0],
        [8, 2, 7]
    ]
    print(s.huarongdao(matrix))
