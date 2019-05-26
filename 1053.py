# coding: utf-8
""" 1053. 交换一次的排列
给出一个正整数的数组 A（元素不一定完全不同），请你返回可在
一次交换（交换两数字 A[i] 和 A[j] 的位置）后得到的、按字典序排列小于 A 的最大排列。
如果无法这么操作，请返回原数组。

示例 1：

输入：[3,2,1]
输出：[3,1,2]
解释：
交换 2 和 1。

示例 2：
输入：[1,1,5]
输出：[1,1,5]
解释：
这已经是最小排列。

示例 3：
输入：[1,9,4,6,7]
输出：[1,7,4,6,9]
解释：
交换 9 和 7。

示例 4：
输入：[3,1,1,3]
输出：[1,1,3,3]

提示：
1 <= A.length <= 10000
1 <= A[i] <= 10000

思路：
分两步走：
从后往前，看是不是依次递减，找到不递减的位置 j ，确认了可调整区间为 [j, n-1]
从 j 往后找，找到比他小的最大位置（因为默认反向即是递增），即为区间第二大数，交换第一大和第二大的数字
"""


class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        if n == 1:
            return A
        j = n - 2
        while j > 0 and A[j] <= A[j + 1]:
            j -= 1
        i = j + 1
        while i < n - 1 and A[i+1] < A[j]:
            i += 1
        A[j], A[i] = A[i], A[j]
        return A


if __name__ == "__main__":
    s = Solution()
    A = [1, 9, 4, 6, 7]
    # A = [3, 1, 1, 3]
    print(s.prevPermOpt1(A))
