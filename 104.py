# coding: utf-8
''' 104. 二叉树的最大深度
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.DFS(root, 1)

    def DFS(self, treeNode, depth):
        """
        :type treeNode: TreeNode
        :rtype: int
        """
        if treeNode.left is not None:
            left_depth = self.DFS(treeNode.left, depth + 1)
        else:
            left_depth = depth
        if treeNode.right is not None:
            right_depth = self.DFS(treeNode.right, depth + 1)
        else:
            right_depth = depth
        return max(left_depth, right_depth)


if __name__ == '__main__':
    s = Solution()
    # nums = [3, 9, 20, null, null, 15, 7]
    root = TreeNode(3)
    current = root
    current.left = TreeNode(9)
    current.right = TreeNode(20)
    current = current.right
    current.left = TreeNode(15)
    current.right = TreeNode(7)
    print(s.maxDepth(root))
