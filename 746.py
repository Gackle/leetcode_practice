# coding: utf-8
""" 746. 使用最小花费爬楼梯

数组的每个索引做为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:
输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。

示例 2:
输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

注意：
cost 的长度将会在 [2, 1000]。
每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。

提示：
动态规划

思路：
一维的动态规划数组解决：
对于一维的数组 dp，对于 dp[i] 表示登上 i 级台阶所需要耗费的最低花费（0≤i≤len(cost)-1）；
那么对于任意的 dp[i] (i≥2) 存在如下状态转移方程：
    dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i])
对于 i<2 的 dp 来说，存在 dp[i] = cost[i]

优化：
一维的动态规划数组实际上可以简化为 n 个递推所需变量，如上面的
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        dp = [1000] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i])
        return dp[-1]


class Solution1(object):
    """ 节省空间DP
    """

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        x = cost[0]
        y = cost[1]
        for i in range(2, len(cost)):
            z = min(x+cost[i], y+cost[i])
            x, y = y, z
        return z


if __name__ == "__main__":
    s = Solution1()
    # cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    # cost = [10, 15, 20]
    cost = [1, 2, 3, 7, 1, 2, 4, 6, 8, 10, 12, 34]
    print(s.minCostClimbingStairs(cost))
