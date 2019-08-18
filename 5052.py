# coding: utf-8
""" 5052. 最大层内元素和

给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。
请你找出层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。

示例：
输入：[1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。
"""

from tree_util import initial_tree, TreeNode


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.queue = [[], []]
        self.count = []
        self.queue[0].append(root)
        self.bfs(0)
        return self.count.index(max(self.count)) + 1

    def bfs(self, i):
        self.count.append(0)
        currentQ = self.queue[i % 2]
        nextQ = self.queue[(i+1) % 2]
        nextQ.clear()
        while currentQ:
            item = currentQ.pop()
            self.count[i] += item.val
            if item.left:
                nextQ.append(item.left)
            if item.right:
                nextQ.append(item.right)
        if nextQ:
            self.bfs(i+1)


if __name__ == "__main__":
    s = Solution()
    l = [1, 7, 0, 7, -8, None, None]
    l = [1, 7, 0, 7, -8, None, None, 4, None, None, None, 11]
    root = initial_tree(l)
    print(s.maxLevelSum(root))
