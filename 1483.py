# encoding: utf-8
"""1483. 树节点的第 K 个祖先
给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。
树的根节点是编号为 0 的节点。
树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。
实现 TreeAncestor 类：

TreeAncestor（int n， int[] parent） 对树和父数组中的节点数初始化对象。
getKthAncestor(int node, int k) 返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节点，返回 -1 。

示例 1：
输入：
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]
输出：
[null,1,0,-1]

解释：
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点

提示：
1 <= k <= n <= 5 * 10^4
parent[0] == -1 表示编号为 0 的节点是根节点。
对于所有的 0 < i < n , 0 <= parent[i] < n 总成立
0 <= node < n 至多查询 5 * 10^4 次
"""
from typing import List
class TreeAncestorTimeout:
    """ 暴力算法超时
    """
    def __init__(self, n: int, parent: List[int]):
        self.parent = parent


    def getKthAncestor(self, node: int, k: int) -> int:
        index = 0
        cur = node
        while index < k and cur != -1:
            cur = self.parent(cur)
            index += 1    
        return cur


class TreeAncestor:
    """ 倍增算法（本质 dp）
    即对树上每个节点都保存一个数组，其存储距某个节点距离为2^i次方的节点
    """
    def __init__(self, n: int, parent: List[int]):
        log = 16  # math.log2(5e4) = 15.609640474436812 即 log(n)
        self.ancestor = [[-1] * log for i in range(n)] # 根节点不能往上查找父节点
        for i in range(1, n):
            self.ancestor[i][0] = parent[i]  # 先维护父节点
        for i in range(1, n):
            self.ancestor[i][0] = parent[i]
            for j in range(1, log):
                self.ancestor[i][j] = self.ancestor[self.ancestor[i][j-1]][j-1]
        


    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(15, -1, -1):
            if k >> i & 1 == 1:
                node = self.ancestor[node][i]
                if node < 0:
                    return -1
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)


if __name__ == '__main__':
    # t = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    t = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    inp = ([3,1],[5,2],[6,3])
    ans = [1,0,-1]
    for i, v in enumerate(inp):
        res = t.getKthAncestor(*v)
        assert res == ans[i], f"[-1, 0, 0, 1, 1, 2, 2] -> {v} except {ans[i]} but got {res}"

    t = TreeAncestor(5,[-1,0,0,0,3])
    inp = ([1,5],[3,2],[0,1],[3,1],[3,5])
    ans = [-1,-1,-1,0,-1]
    for i, v in enumerate(inp):
        res = t.getKthAncestor(*v)
        assert res == ans[i], f"[-1,0,0,0,3] -> {v} except {ans[i]} but got {res}"
    
    t = TreeAncestor(4,[-1,2,3,0])
    inp = ([2,3],[2,2],[2,1])
    ans = [-1,0,3]
    for i, v in enumerate(inp):
        res = t.getKthAncestor(*v)
        assert res == ans[i], f"[-1,2,3,0] -> {v} except {ans[i]} but got {res}"

    print("You Pass!")