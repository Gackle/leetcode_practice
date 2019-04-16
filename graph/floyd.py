# coding: utf-8
""" Floyd 算法
求多源最短路径 —— 确定任意两点间的最短路径
思路：
  floyd 本质上是动态规划的一种实现，适合正权边和负权边的有向图或无向图（不适用于负权环），稠密图效果最佳
  通过在任意两点之间添加新的中转点使得两点间的路程缩短
时间复杂度:
  O(n^3) —— 因为是三重循环
空间复杂度:
  O(n^2)
"""
from sys import maxsize as MAXINT


def floyd_for_matrix(matrix, begin, end):
    """ 基于邻接矩阵
    :type matrix: List[List[int]]
    :type begin: int
    :type end: int
    :rtype: int
    """
    path = matrix[:]
    N = len(matrix[0])
    for k in range(N):
        for i in range(N):
            for j in range(N):
                path[i][j] = min(path[i][j], path[i][k] + path[k][j])
    return path[begin][end]


def floyd_for_dict(vertical, edges, source, target):
    """ 基于邻接表
    :type vertical: List[int]
    :type edges: dict
    :type source: str
    :type target: str
    """
    # BEGIN 构建二维矩阵
    N = len(vertical)
    path = [[MAXINT]*N for i in range(N)]
    begin = vertical.index(source)
    end = vertical.index(target)
    for v in edges:
        for vn in edges[v]:
            path[vertical.index(v)][vertical.index(vn)] = edges[v][vn]
    # END 構建二維矩陣
    for k in range(N):
        for i in range(N):
            for j in range(N):
                path[i][j] = min(path[i][j], path[i][k] + path[k][j])
    return path[begin][end]


if __name__ == "__main__":
    matrix = [
        [0, 6, 3, MAXINT, MAXINT, MAXINT],
        [6, 0, 2, 5, MAXINT, MAXINT],
        [3, 2, 0, 3, 4, MAXINT],
        [MAXINT, 5, 3, 0, 2, 3],
        [MAXINT, MAXINT, 4, 2, 0, 5],
        [MAXINT, MAXINT, MAXINT, 3, 5, 0]
    ]

    vertical = ["A", "B", "C", "D", "E", "F"]
    edges = {
        "A": {"B": 6, "C": 3},
        "B": {"A": 6, "C": 2, "D": 5},
        "C": {"A": 3, "B": 2, "D": 3, "E": 4},
        "D": {"B": 5, "C": 3, "E": 2, "F": 3},
        "E": {"C": 4, "D": 2, "F": 5},
        "F": {"D": 3, "E": 5}
    }
    # print(floyd_for_matrix(matrix, 0, 5))
    print(floyd_for_dict(vertical, edges, "A", "F"))
