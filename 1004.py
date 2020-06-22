# -*- coding: utf-8 -*-
""" 1004. 最大连续1的个数 III
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

返回仅包含 1 的最长（连续）子数组的长度。

思路：双指针/滑动窗口

示例 1：

输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6

解释:
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。

示例 2：
输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
 

提示：

- 1 <= A.length <= 20000
- 0 <= K <= A.length
- A[i] 为 0 或 1 
"""
from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        max_len = 0
        zero_count = 0
        left = 0
        right = 0
        n = len(A)
        while left < n:
            while right < n and zero_count <= K:
                if A[right] == 0:
                    zero_count += 1
                right += 1
            max_len = max(max_len, right - left - max(0, zero_count - K))
            # 缩短逻辑
            if right == n:
                # 右指针到达末尾，退出
                break
            while left <= right and A[left] != 0:
                left += 1
            left += 1
            zero_count -= 1
        return max_len


class Solution1():
    def longestOnes(self, A: List[int], K: int) -> int:
        ans = i = 0
        for j in range(len(A)):
            if A[j] == 0:ans += 1
            if ans > K:
                if A[i] == 0:ans -= 1
                i += 1
        return (j - i + 1)


if __name__ == "__main__":
    s = Solution1()
    # A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    # K = 2
    # assert s.longestOnes(A, K) == 6, f'case 1: {s.longestOnes(A, K)} neq 6'
    A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    K = 3
    assert s.longestOnes(A, K) == 10, f'case 2: {s.longestOnes(A, K)} neq 10'
    # A = [0, 0, 0, 1]
    # K = 4
    # assert s.longestOnes(A, K) == 4, f'case 3: {s.longestOnes(A, K)} neq 4'
