# -*- conding: utf-8 -*-
""" 56. 合并区间
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """ 倒叙遍历的思路，接近 O(n^2) ，运行速度和下面的思路差不多估计把排序的时间算上了也是 O(n^2) 左右
        因为在原数组上增删，所以内存消耗较低
        """
        n = len(intervals)
        if n < 2:
            return intervals
        i = n - 2
        while i >= 0:
            cur = intervals[i]
            j = i + 1
            while j < len(intervals):
                post = intervals[j]
                if not (cur[0] > post[1] or cur[1] < post[0]):
                    cur = [min(cur[0], post[0]), max(cur[1], post[1])]
                    del intervals[j]
                    j -= 1
                j += 1
            intervals[i] = cur
            i -= 1
        return intervals


class Solution1:
    """ 先排序的思路
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == "__main__":
    s = Solution()
    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]  # [[1,10]]
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]  # [[1,6],[8,10],[15,18]]
    print(s.merge(intervals))
