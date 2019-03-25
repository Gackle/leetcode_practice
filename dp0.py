# coding: utf-8
""" 国王与金矿 - （类似的还有找零钱问题）
DP 的背包问题模型
有一个国家发现了5座金矿，每座金矿的黄金储量不同，需要参与挖掘的工人数也不同。
参与挖矿工人的总数是10人。每座金矿要么全挖，要么不挖，不能派出一半人挖取一半金矿。
要求用程序求解出，要想得到尽可能多的黄金，应该选择挖取哪几座金矿？

“将前i件物品放入容量为v的背包中”这个子问题，若只考虑第i件物品的策略（放或不放），那么就可以转化为一个只牵扯前i-1件物品的问题。
如果不放第i件物品，那么问题就转化为“前i-1件物品放入容量为v的背包中”；如果放第i件物品，那么问题就转化为“前i-1件物品放入剩下的容量为v-c[i]的背包中”，
此时能获得的最大价值就是f [i-1][v-c[i]]再加上通过放入第i件物品获得的价值w[i]。

则其状态转移方程便是：f[i][v]=max{f[i-1][v],f[i-1][v-c[i]]+w[i]}

具体：填充行为金矿数，列为工人数的二维表格
时间复杂度为 O(n*len(p)), 空间复杂度也一样。
可以使用滚动数组优化空间复杂度为 O(n)

注意，因为空间复杂度和时间复杂度在 DP 中都和 n 成正比，而简单递归却和 n 无关，因此
对于工人数量很多（n很大）的时候，动态规划不如简单递归
"""


class Solution(object):
    def minerAndQuarts(self, n, p):
        """
        :type n: int
        :type p: List[(int, int)]
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in range(len(p))]
        # 外循环为金矿数量，内循环为工人数
        for i, v in enumerate(p):  # 金矿数从第1个开始
            for j in range(n+1):  # 分配工人数从 0 到 n
                if i == 0:
                    dp[i][j] = v[0] if j >= v[1] else 0
                else:
                    if j >= v[1]:  # 分配的工人数大于等于第i个矿所需的工人数
                        dp[i][j] = max(dp[i-1][j], dp[i-1][j-v[1]]+v[0])
                    else:          # 分配的工人数小于第i个矿所需的工人数
                        dp[i][j] = max(dp[i-1][j], 0)
        return dp[len(p)-1][n]


if __name__ == "__main__":
    s = Solution()
    p = [(400, 5), (500, 5), (200, 3), (300, 4), (350, 3)]
    n = 10
    print(s.minerAndQuarts(n, p))