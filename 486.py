# coding: utf-8
""" 486. 预测赢家
给定一个表示分数的非负整数数组。
玩家1从数组任意一端拿取一个分数，随后玩家2继续从剩余数组任意一端拿取分数，然后玩家1拿，……。
每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。
最终获得分数总和最多的玩家获胜。

给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

题解：这是属于 DP 的问题，可以看作是跳楼梯的一个变种
既然是 DP 问题，最重要的是得到递归公式（状态转移方程）
假设 dp[i][j] 为 player1 从数组 a 的第 i 到第 j 所能拿到的最大数字和
则会有 player2 能拿到的最大数字和为 max(dp[i+1][j], dp[i][j-1])
设数组 a 从 i 到 j 的数字和为 sum[i, j]
这里有一个非常巧妙地思路 —— **反过来得到递推公式**，利用 player2 反推 player1 的数字和，即：
dp[i][j] = max(sum[i+1, j]-dp[i+1][j]+a[i], sum[i, j-1]-dp[i][j-1]+a[j])
化简一下得到:
dp[i][j] = max(sum[i, j]-dp[i+1][j], sum[i, j]-dp[i][j-1])
"""
from typing import List, Tuple, Dict, TextIO


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        end = len(nums)
        dp = [[0]*end for i in range(len(nums))]
        # 以列为最外层，同时行倒序遍历
        for j in range(0, end):
            dp[j][j] = nums[j]
            i = j-1
            while i >= 0:
                dp[i][j] = max(sum(nums[i:j+1])-dp[i+1][j], sum(nums[i:j+1])-dp[i][j-1])
                i -= 1
        return True if dp[0][end-1] >= sum(nums)/2 else False


if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 233, 7]
    print(s.PredictTheWinner(nums))
