# coding: utf-8

""" 932. 漂亮数组
对于某些固定的 N，如果数组 A 是整数 1, 2, ..., N 组成的排列，使得：
对于每个 i < j，都不存在 k 满足 i < k < j 使得 A[k] * 2 = A[i] + A[j]。
那么数组 A 是漂亮数组。

给定 N，返回任意漂亮数组 A（保证存在一个）。

示例 1：
输入：4
输出：[2,1,4,3]

示例 2：
输入：5
输出：[3,1,2,5,4]

提示：
1 <= N <= 1000

思路：主要是找规律
（1）奇数+偶数 肯定 不等于 2xA[k] 
（2）2×奇数 + 2×偶数 肯定也满足（1），即不等于 2x2xA[k] 
（3）2×奇数-1 + 2×偶数-1 肯定也满足（1），即不等于 2x(2xA[k]-1) 

那么递归式就有了，f(n)=f(n/2+n%2)x2 [join] f(n/2+n%2)x2-1
"""


class Solution:
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        if N == 1:
            return [1]
        else:
            l = self.beautifulArray(N//2)
            r = self.beautifulArray(N-N//2)
            return [x*2 for x in l] + [x*2-1 for x in r]

if __name__ == '__main__':
    s = Solution()
    N = 4
    print(s.beautifulArray(N))
