# coding: utf-8
""" 802. 找到最终的安全状态

在有向图中, 我们从某个节点和每个转向处开始, 沿着图的有向边走。 如果我们到达的节点是终点 (即它没有连出的有向边), 我们停止。
现在, 如果我们最后能走到终点，那么我们的起始节点是最终安全的。 
更具体地说, 存在一个自然数 K,  无论选择从哪里开始行走, 我们走了不到 K 步后必能停止在一个终点。
哪些节点最终是安全的？ 结果返回一个有序的数组。

该有向图有 N 个节点，标签为 0, 1, ..., N-1, 其中 N 是 graph 的节点数.  图以以下的形式给出: graph[i] 是节点 j 的一个列表，满足 (i, j) 是图的一条有向边。

示例：
输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
输出：[2,4,5,6]

提示：
- graph 节点数不超过 10000.
- 图的边数不会超过 32000.
- 每个 graph[i] 被排序为不同的整数列表， 在区间 [0, graph.length - 1] 中选取。

关键：
深度优先 DFS | 拓扑排序
"""
from typing import List


class Solution:
    """ DFS 解法，需要 color 来记录遍历点的状态（未处理，不安全，安全）
    不安全状态指 【这个点在一个环中】，因此寻找安全状态就是找到不在环中的点
    所以：如果一个点的存在后继点是不安全的，那么它自己也是不安全的，只有当所有后继点是安全的，它自己才是安全的
    """

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        result = []
        color = [0] * n  # 颜色状态表 0 表示灰色待验证 1 表示存在环 2 表示不存在环

        def dfs(i: int) -> bool:
            if color[i]:
                return color[i] == 2  # 已经访问过的返回是否存在环
            color[i] = 1  # 所有点默认都是不安全的（存在环）
            for j in graph[i]:
                if color[j] == 1 or not dfs(j):
                    return False
            color[i] = 2  # 遍历了所有路径都不存在环
            return True

        for i in range(n):
            if dfs(i):
                result.append(i)

        return result


if __name__ == "__main__":
    s = Solution()
    # graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    # graph = [[0, 1], []]
    # graph = [[1], [2], [3], [4], [0]]  # []
    # graph = [[1], [2], [3], [4, 5], [0], []]  # [5]
    # graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]  # [4]
    # graph = [[0], [1, 2, 3, 4], [1, 3, 4], [2, 4], [2]]
    graph = [[1], [1]]
    print(s.eventualSafeNodes(graph))
