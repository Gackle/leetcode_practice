# coding: utf-8
"""1524. 和为奇数的子数组数目
给你一个整数数组 arr 。请你返回和为 奇数 的子数组数目。
由于答案可能会很大，请你将结果对 10^9 + 7 取余后返回。

示例 1
输入- arr = [1,3,5]
输出- 4
解释：所有的子数组为 [[1],[1,3],[1,3,5],[3],[3,5],[5]] 。
所有子数组的和为 [1,4,9,3,8,5].
奇数和包括 [1,9,3,5] ，所以答案为 4 。

示例 2
输入 - arr = [2,4,6]
输出 - 0
解释：所有子数组为 [[2],[2,4],[2,4,6],[4],[4,6],[6]] 。
所有子数组和为 [2,6,12,4,10,6] 。
所有子数组和都是偶数，所以答案为 0 。

示例 3
输入 - arr = [1,2,3,4,5,6,7]
输出 - 16

示例 4
输入 - arr = [100,100,99,99]
输出 - 4

示例 5
输入 - arr = [7]
输出 - 1

提示：

1 <= arr.length <= 10^5
1 <= arr[i] <= 100
"""
from typing import List

class Solution:
    def numOfSubarrays_timeout(self, arr: List[int]) -> int:
        """ deprecated: 超时
        """
        n = len(arr)
        pre_sum = [0] * (n+1)
        ans = 0

        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + arr[i]
        
        for i in range(1, n+1):
            for j in range(i):
                if (pre_sum[i] - pre_sum[j]) % 2 == 1:
                    ans += 1
        return ans % (1e+9+7)
    
    def numOfSubarrays(self, arr: List[int]) -> int:
        """ 优化：odd + odd => even / even + even => even / odd + even => odd
        耗时：$O(n)$
        """
        n = len(arr)
        ans = 0
        even = 0  # 以 arr[i] 结尾的子数组和为偶数的个数
        odd = 0  # 以 arr[i] 结尾的子数组和为奇数的个数

        for i in range(n):
            if arr[i] % 2:  # odd - 因为有优化公式，因为 arr[i] 本身为 odd ，所以和前面的 sum(even) 都可以得到 odd ，而和前面的 sum(odd) 都只能得到 even，+1 是为了处理本身自己 [arr[i]] 形式的子数组
                odd, even = even + 1, odd
            else:  # even - 根据优化公式，arr[i] 为 even ，和所有的 even 都只能得到 even 同时还要包括他自身单元素子数组所以 +1 ，和前面的 sum(odd) 都能得到 odd 所以新的数字不变
                odd, even = odd, even + 1
            ans += odd  # 累加每个 arr[i] 结尾的子数组的奇数和个数
        return int(ans % (1e9+7))

if __name__ == "__main__":
    s = Solution()
    examples = [
        ([1, 3, 5], 4),
        ([2, 4, 6], 0),
        ([1, 2, 3, 4, 5, 6, 7], 16),
        ([100, 100, 99, 99], 4),
        ([7], 1),
    ]

    for row in examples:
        lst, res = row
        ans = s.numOfSubarrays(lst)
        assert ans == res, f"except {res} but got {ans}"

    print("You Pass!")