# coding: utf-8
""" Dijkstra 算法
求单源最短路径 —— 确定一个源点，到其余所有结点的最短路径
思路：
  - dijkstra 本质上的思想是贪心,它只适用于不含负权边的图.
流程：
    1. 初始化 dis[start]=0, dis[start]=0, 其余节点的 dis 值为无穷大
    2. 找一个未被标记的且 dis 值最小的节点 x, 标记节点 x
    3. 遍历 x 的所有出边 (x,y,z) ,若 dis[y]>dis[x]+z, 则令dis[y]=dis[x]+z
    4. 重复 2，3 两步, 直到所有点都被标记
时间复杂度：
  O(n2)
参考：
  - https://www.cnblogs.com/mingjiatang/p/5974451.html
  - https://www.cnblogs.com/wangyuliang/p/9216365.html
补充：
  - 边数 M 远小于点数 N 的平方的图为稀疏图，反之为稠密图
  - 可以使用堆加速找到离起始点最近的点：O(logN)
  - 对于稠密图，使用邻接矩阵；对于稀疏图，邻接表效率更高
"""
from sys import maxsize as MAXINT


def dijkstra_for_matrix(M, source, target):
    """ 基于邻接矩阵
    :type M: List[List[int]]
    :rtype: int
    """
    N = len(M[0])
    # 已访问列表
    visited = [source]
    # source 为原点的距离表
    dis = [MAXINT] * N
    dis[source] = 0
    # source 为原点的路径表
    path = [""] * N
    path[source] = str(source)
    # BEGIN 具体算法
    cur = source
    while len(visited) < N:
        min_value = MAXINT
        for index, node in enumerate(M[cur]):
            if index not in visited:
                if dis[index] > dis[cur] + node:
                    dis[index] = dis[cur] + node
                    path[index] = path[cur] + str(index)
        # 找出这一轮的最小点
        for index, node in enumerate(dis):
            if index not in visited and node <= min_value:
                min_value = node
                cur = index
        visited.append(cur)
    return dis[target]
    


def dijkstra_for_dict(vertical, edges, source, target):
    """ 基于邻接表
    :type vertical: List[str]
    :type edges: dict
    :type source: str
    :type target: str
    :rtype: int
    """
    # 已访问列表（贪心累积）
    visited = [source]
    # 距离哈希表
    dis = {k: MAXINT if k != source else 0 for k in vertical}
    # 路径哈希表
    path = {k: "" if k != source else source for k in vertical}
    vertical.remove(source)
    # 具体算法
    current = source
    while vertical:
        min_value = MAXINT
        for node in edges[current].keys():
            if node in visited:
                continue
            updated = dis[current] + edges[current][node]
            if dis[node] > updated:
                dis[node] = updated
                path[node] = path[current] + node
        for i in vertical:
            if i not in visited and dis[i] <= min_value:
                min_value = dis[i]
                current = i
        visited.append(current)
        vertical.remove(current)
    return dis[target]


if __name__ == '__main__':
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
    print(dijkstra_for_matrix(matrix, 1, 5))
    print(dijkstra_for_dict(vertical, edges, "B", "F"))
