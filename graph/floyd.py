# coding: utf-8
""" Floyd 算法
求多源最短路径 —— 确定任意两点间的最短路径
思路：
  floyd 本质上是动态规划的一种实现，适合正权边和负权边的有向图或无向图（不适用于负权环），稠密图效果最佳
  通过在任意两点之间添加新的中转点使得两点间的路程缩短
时间复杂度:
  O(n^3)
空间复杂度:
  O(n^2)
"""


def floyd_for_matrix(matrix, begin, end):
    path = matrix[:]
    


def floyd_for_dict(vertical, edges, source, target):
    # 二维动态规划矩阵（空间复杂度 O(n^2)）
    pass


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
