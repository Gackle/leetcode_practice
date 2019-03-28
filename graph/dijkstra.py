# coding: utf-8
""" Dijkstra 算法
求最短路径：确定一个源点，求到目标点的最短路径
"""

def dijkstra(M, source, target):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    path = []
