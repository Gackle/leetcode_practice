# coding: utf-8
""" 114. 二叉树展开为链表
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
from tree_util import TreeNode, initialTree


class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        :type node: TreeNode
        """
        if root is None:
            return
        head, tail = self.dfs(root)
        cur = head
        # 测试代码
        while cur:
            print(cur.val)
            cur = cur.right

    def dfs(self, node):
        """
        :type node: TreeNode
        :rtype: (TreeNode, TreeNode)
        """
        if not (node.left or node.right):
            return node, node
        if node.left:
            # lts: left tree start, lte: left tree end
            lts, lte = self.dfs(node.left)
        if node.right:
            # rts: right tree start, rte: right tree end
            rts, rte = self.dfs(node.right)
        # 迭代合并
        if node.left and node.right:
            node.left = None
            node.right = lts
            lte.right = rts
            return node, rte
        if node.left and not node.right:
            node.left = None
            node.right = lts
            return node, lte
        if not node.left and node.right:
            node.left = None
            node.right = rts
            return node, rte


if __name__ == "__main__":
    # l = [1, 2, 5, 3, 4, None, 6]
    l = [1, 2, 3]
    root = initialTree(l)
    s = Solution()
    s.flatten(root)
