# coding: utf-8

""" 172. 阶乘后的零

给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:
输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。

示例 2:
输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.

说明: 你算法的时间复杂度应为 O(log n) 。

思路：要求末尾有多少个零，则该数应为x*10k 的形式等于x*(2k*5k)
也就是求该数分解质因子后有几个5就行，：如1*2*3*4*5=1*2*3*2*2*5（里面有一个5）所以结果为1个0
"""


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        while n > 1:
            n //= 5
            total += n
        return total


if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.trailingZeroes(n))
