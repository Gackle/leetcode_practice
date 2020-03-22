# coding: utf-8
""" 945. 使数组唯一的最小增量
给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
返回使 A 中的每个值都是唯一的最少操作次数。

示例 1:
输入：[1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
示例 2:
输入：[3,2,1,2,1,7]
输出：6
解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。

提示：
0 <= A.length <= 40000
0 <= A[i] < 40000

思路：
1. 计数
当我们找到一个没有出现过的数的时候，将之前某个重复出现的数增加成这个没有出现过的数。
注意，这里 「之前某个重复出现的数」 是可以任意选择的，它并不会影响最终的答案，
因为将 P 增加到 X 并且将 Q 增加到 Y，与将 P 增加到 Y 并且将 Q 增加到 X 都需要进行 (X + Y) - (P + Q) 次操作。
注意我们的数据可能会递增到 80000 。这是因为在最坏情况下，数组 A 中有 40000 个 40000，
这样要使得数组值唯一，需要将其递增为 [40000, 40001, ..., 79999]，因此用来统计的数组需要开到 80000
时空复杂度都为 O(L) ，其中 L 的数量级是数组 A 的长度加上其数据范围内的最大值

2. 排序
我们先对 A 进行排序，然后进行线性扫描，会得到：
1. A[i-1] = A[i] ， 代表 A[i] 重复出现，重复个数 taken + 1 ；
2. A[i-1] != A[i] ， 则代表 (A[i-1]+1 ~ A[i]-1) 这个范围内的数都没有出现过可以被利用起来。则我们可以利用的个数 given = min(taken, A[i]-A[i-1]-1)
   如果 taken 较大无法完全消耗完，可以将这些数变为区间 ([A[n−1]+1, ∞) 中的数，其中 A[n - 1] 是数组 A 中的最后一个数。
"""
from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        hash_table = [0] * 80000
        for i in A:
            hash_table[i] += 1

        ans = taken = 0

        for i in range(80000):
            if hash_table[i] >= 2:
                taken += (hash_table[i] - 1)
                ans -= i * (hash_table[i] - 1)
            elif taken > 0 and hash_table[i] == 0:
                taken -= 1
                ans += i

        return ans


class Solution1:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        A.append(999999)  # 加一个超出范围的数，是为了确保最后如果有重复数字的时候也交给循环处理
        ans = taken = 0
        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                taken += 1
                ans -= A[i]
            else:
                give = min(taken, A[i]-A[i-1]-1)
                ans += give * (give + 1) // 2 + give * A[i-1]  # 等差数列求和
                taken -= give

        return ans


if __name__ == "__main__":
    s = Solution1()
    # A = [3, 2, 1, 2, 1, 7]
    A = [1, 2, 2]
    print(s.minIncrementForUnique(A))
