# coding: utf-8
""" 973. 最接近原点的 K 个点

我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。
（这里，平面上两点之间的距离是欧几里德距离。）
你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

示例 1：
输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]

示例 2：
输入：points = [[3,3],[5,-1],[-2,4]], K = 2
输出：[[3,3],[-2,4]]

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000

提示：
排序 分治算法
"""


class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        from queue import PriorityQueue
        distance = PriorityQueue()
        result = list()
        for point in points:
            d = point[0]**2 + point[1]**2
            distance.put((d, point))

        for _ in range(K):
            result.append(distance.get()[1])

        return result


class Solution2:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:K]


if __name__ == "__main__":
    s = Solution2()
    K = 2
    points = [[3, 3], [5, -1], [-2, 4]]
    print(s.kClosest(points, K))
