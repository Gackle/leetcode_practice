# coding: utf-8
""" 96. 不同的二叉搜索树
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

提示：树 动态规划

思路：
n = 1 时，二叉搜索树只有 1 个；
n = 2 时，二叉搜索树有两个：
  1         2
   \       /
    2      1

对于 n = 3, 则有 f[1, 3] = f[2, 3] + f[1, 2] + (f[1, 1]/f[3, 3]) 的规律，
其中 f[i,j] 表示从 i 到 j 组成的二叉搜索树的个数，因此，状态转移方程为: 
   f[i, j] = f[i, j-1] * 1 + f[i,j-2] * f[j,j] + f[i, j-3] * f[j-1, j] + .... 1 * f[i+1, j]
           =》以 j 为根 + 以 j-1 为根 + 以 j-2 为根 + .... 以 i 为根
这里利用了一个二叉搜索树的特点：一个节点的左子树上的全部值都会比右子树上的全部值都小，
对于连续的 1~n，实际上，可以将他们划分为两个连续的序列来构成一棵树
"""


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
        for i in range(1, n+2)[::-1]:
            dp[i][i] = 1
            if i <= n:
                dp[i][i+1] = 2
            for j in range(i+2, n+2):
                if dp[i][j] != 0:
                    continue
                dp[i][j] += (dp[i+1][j] + dp[i][j-1])
                d = 0
                while d < j-i-1:
                    dp[i][j] += dp[i][i+d]*dp[i+2+d][j]
                    d += 1
        return dp[1][n]


if __name__ == "__main__":
    s = Solution()
    n = 0
    print(s.numTrees(n))
