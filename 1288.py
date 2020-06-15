# -*- coding: utf-8 -*-
""" 1288. 删除被覆盖区间
给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。
只有当 c <= a 且 b <= d 时，我们才认为区间 [a,b) 被区间 [c,d) 覆盖。
在完成所有删除操作后，请你返回列表中剩余区间的数目。

 

示例：
输入：intervals = [[1,4],[3,6],[2,8]]
输出：2
解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。

提示：​​​​​​

1 <= intervals.length <= 1000
0 <= intervals[i][0] < intervals[i][1] <= 10^5
对于所有的 i != j：intervals[i] != intervals[j]
"""
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 关键：按照起始点大小进行排序，如果起点大小相同，则终点越大排越前（即同起点区间越大越前）
        intervals.sort(key=lambda u: (u[0], -u[1]))
        n = len(intervals)
        ans, rmax = n, intervals[0][1]
        for i in range(1, n):
            if intervals[i][1] <= rmax:
                # 关键：如果比 rmax 要大，隐含条件不可能同起点，同时因为比他大，所以这是一个新的备选区间
                ans -= 1
            else:
                rmax = max(rmax, intervals[i][1])
        return ans


if __name__ == "__main__":
    s = Solution()
    # intervals = [[1, 4], [3, 6], [2, 8]]  # 2
    # intervals = [[0, 10], [5, 12]]  # 2
    # intervals = [[3, 10], [4, 10], [5, 11]]  # 2
    # intervals = [[1, 2], [1, 4], [3, 4]]  # 1
    intervals = [[0, 10], [10, 11], [10, 15]]
    print(s.removeCoveredIntervals(intervals))
