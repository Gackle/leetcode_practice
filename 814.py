# coding: utf-8
""" 814. 二叉树剪枝

给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。

返回移除了所有不包含 1 的子树的原二叉树。

( 节点 X 的子树为 X 本身，以及所有 X 的后代。)
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        output = self.dfs(root)
        return root

    def dfs(self, node):
        """
        :type node: TreeNode
        :rtype: bool
        """
        if not node.left and not node.right:
            return node.val == 1
        left_bool = False
        right_bool = False
        if node.left:
            left_bool = self.dfs(node.left)
        if node.right:
            right_bool = self.dfs(node.right)
        if left_bool == False:
            node.left = None
        if right_bool == False:
            node.right = None
        return left_bool or right_bool or (node.val == 1)




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
    li = [1, None, 0, 0, 1]
    root = initialTree(li)
    print(s.pruneTree(root))
