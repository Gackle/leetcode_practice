# coding: utf-8
""" 63. 不同路径 II
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？


网格中的障碍物和空位置分别用 1 和 0 来表示。
说明：m 和 n 的值均不超过 100。

思路：动态规划，状态为 m[i][j] 表示从 obstacleGrid[0][0] 到 obstacleGrid[i][j]
所有可能的路径，则状态转移方程为：
            0  if(obstacleGrid[i][j] == 1)
m[i][j] =
            m[i-1][j] + m[i][j-1] if(obstacleGrid == 0)
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 默认的到起始点只有一条路 ~
        dp[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    s = Solution()
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    r = s.uniquePathsWithObstacles(obstacleGrid)
    assert r == 2, f"case 1 {r} neq 2"
