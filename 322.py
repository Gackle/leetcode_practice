# coding: utf-8
""" 322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1

示例 2:
输入: coins = [2], amount = 3
输出: -1

提示：动态规划

思路：
对于一维的数组 dp，有 dp[n] = min(dp[n-i]+1) (n <= amount, i ∈ coins)的状态转移方程
其中 dp[n] 表示 n 块钱需要的最小的硬币数
其中要注意处理 n<i 的情况，很常规的一维 dp 问题（0/1背包）
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0 for _ in range(amount+1)]
        for n in range(1, amount+1):
            flag = False  # 是否存在 i 的面值比 n 要小，用于减少后面dp[n]赋值排除
            min_count = amount+1  # 假如全部都为 1 元，则最大 dp[n] < amount+1 的取巧方法
            for i in coins:
                if i <= n and dp[n-i] != -1:
                    flag = True
                    min_count = min(min_count, (dp[n-i] + 1))
            dp[n] = min_count if flag else -1
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    coins = [2, 5]
    amount = 4
    print(s.coinChange(coins, amount))
