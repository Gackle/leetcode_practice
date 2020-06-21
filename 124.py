# coding: utf-8
""" 124. 二叉树中的最大路径和

给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6

题解：对于每个节点都求她的最大贡献度 maxGain ， 叶子节点的最大贡献度为它本身，而非叶子节点等于它本身以及其子节点中 maxGain 的和
然后递归 DFS ，中间保存一个 maxSum 作为结果
"""
from tree_util import TreeNode, initial_tree
import sys


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        maxSum = -sys.maxsize

        def maxGain(node: TreeNode) -> int:
            """ 求某节点的最大贡献度
            """
            nonlocal maxSum
            if not node:
                return 0
            leftGain = maxGain(node.left)
            rightGain = maxGain(node.right)
            # 需要返回的该节点最大贡献度 （为单一子树）
            nodeGain = node.val + max(0, leftGain, rightGain)
            # 计算该节点的最大路径和要把两个子树都算上
            nodeSum = node.val + max(0, leftGain) + max(0, rightGain)
            maxSum = max(maxSum, nodeSum)
            return nodeGain

        maxGain(root)

        return maxSum


if __name__ == "__main__":
    s = Solution()
    # _list = [1, 2, 3]
    # root = initial_tree(_list)
    # assert s.maxPathSum(root) == 6, 'case 1'
    # _list = [-10, 9, 20, None, None, 15, 7]
    # root = initial_tree(_list)
    # assert s.maxPathSum(root) == 42, 'case 2'
    # _list = [1]
    # root = initial_tree(_list)
    # assert s.maxPathSum(root) == 1, 'case 3'
    _list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    root = initial_tree(_list)
    assert s.maxPathSum(root) == 48, f'case 4: {s.maxPathSum(root)} neq 48'
    _list = [9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6]
    root = initial_tree(_list)
    assert s.maxPathSum(root) == 16, f'case 5: {s.maxPathSum(root)} neq 16'
