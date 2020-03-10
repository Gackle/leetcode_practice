# coding: utf-8
""" 1013. 将数组分成和相等的三个部分
给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

示例 1：
输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

示例 2：
输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false

示例 3：
输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

思路：如果 sum 不是 3 的倍数，直接返回 false；然后双指针往中间靠拢，如果两部分都能得到 1/3 则返回true
注意：1. part 为 0 的情况，主要是如果是自己累加则容易出错（因为和一开始为 0），用 sum 倒不会有这个问题
     2. 注意左右指针的大小关系，不仅仅是右指针要大于左指针，而是右指针至少大于左指针+1（中间数组最少有一个元素）
"""
from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        n = len(A)
        total = sum(A)
        if total % 3:
            return False
        part = total // 3
        left = -1
        left_sum = 0
        right = n
        right_sum = 0
        while left < n - 1:
            left += 1
            left_sum += A[left]
            if left_sum == part:
                break
        if left >= n - 1:
            return False
        while right > left:
            right -= 1
            right_sum += A[right]
            if right_sum == part:
                break
        if right <= left + 1:
            return False
        return True


class Solution1:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        n = len(A)
        total = sum(A)
        if total % 3:
            return False
        part = total // 3
        left = 0
        right = n - 1
        while left < n - 1:
            if sum(A[:left+1]) == part:
                break
            left += 1
        if left > n - 2:
            return False
        while right > left + 1:
            if sum(A[right:]) == part:
                break
            right -= 1
        if right <= left + 1:
            return False
        return True


if __name__ == "__main__":
    s = Solution1()
    A = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]  # True
    # A = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]  # False
    # A = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]  # True
    # A = [14, 6, -10, 2, 18, -7, -4, 11]  # False
    # A = [1, -1, 1, -1]  # False
    # A = [10, -10, 10, -10, 10, -10, 10, -10]  # True
    print(s.canThreePartsEqualSum(A))
