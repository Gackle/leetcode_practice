# coding: utf-8
''' 538. 把二叉搜索树转换为累加树

给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        max_num = self.searchNode(root, 0)
        print(max_num)
        return root

    def searchNode(self, node, add_value):
        '''
        :type node: TreeNode
        :type add_value: int
        :rtype: int
        '''
        if node.right:
            right_total_value = self.searchNode(node.right, add_value)
            node.val += right_total_value
        else:
            node.val += add_value
        return self.searchNode(node.left, node.val) if node.left else node.val


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(5)
    tree.left = TreeNode(2)
    tree.right = TreeNode(13)
    tree.right.right = TreeNode(16)
    tree.right.left = TreeNode(10)
    tree.right.left.left = TreeNode(7)
    tree.right.left.right = TreeNode(12)
    # tree = TreeNode(0)
    # tree.left = TreeNode(-1)
    # tree.right = TreeNode(2)
    # tree.left.left = TreeNode(-3)
    # tree.right.right = TreeNode(4)
    print(s.convertBST(tree))
