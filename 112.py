# coding: utf-8
""" 112. 路径总和

给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。
"""


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.dfs(root, 0, sum)

    def dfs(self, node, current, total):
        """
        :type node: TreeNode
        :type current: int
        :type sum: int
        :rtype: bool
        """
        if not node.left and not node.right:
            return (current + node.val) == total
        left_bool = self.dfs(node.left, current + node.val, total) if node.left else False
        right_bool = self.dfs(node.right, current + node.val, total) if node.right else False

        return left_bool or right_bool


def initialTree(li):
    '''
    :type li: List[int]
    '''
    root = buildTree(TreeNode(li[0]), 0, li)
    return root


def buildTree(parent: TreeNode, i: int, li: list) -> TreeNode:
    left = 2 * i + 1 if i > 0 and li[i - 1] is not None or i == 0 else i + 1
    right = 2 * i + 2 if i > 0 and li[i - 1] is not None or i == 0 else i + 2
    if left < len(li) and li[left] is not None:
        parent.left = buildTree(TreeNode(li[left]), left, li)
    else:
        parent.left = None
    if right < len(li) and li[right] is not None:
        parent.right = buildTree(TreeNode(li[right]), right, li)
    else:
        parent.right = None
    return parent


if __name__ == "__main__":
    s = Solution()
    nums = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    nums = []
    root = initialTree(nums)
    sums = 22
    sums = 1
    print(s.hasPathSum(root, sums))
