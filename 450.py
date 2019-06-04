# coding: utf-8
""" 450. 删除二叉搜索树中的节点

给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

示例:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7

思路：
二叉搜索树的性质
果然题目越长越简单
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_util import initialTree, TreeNode


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        def search(parent: TreeNode, node: TreeNode, target: int):
            if node.val == target:
                return (parent, node)
            if not node.left and not node.right:
                return (parent, None)
            if node.val > target:
                return search(node, node.left, target) if node.left else (parent, None)
            if node.val < target:
                return search(node, node.right, target) if node.right else (parent, None)

        tree_parent = TreeNode(-1)
        tree_parent.right = root
        target_parent, target_node = search(tree_parent, root, key)
        if target_node == root:
            p = root.right
            while p.left:
                p = p.left
            p.left = root.left
            return root.right
        if target_node:
            # 找到了
            if target_parent.left == target_node:
                target_parent.left = target_node.left
                p = target_node.left
                while p.right:
                    p = p.right
                p.right = target_node.right
            else:
                target_parent.right = target_node.right
                p = target_node.left
                while p.left:
                    p = p.left
                p.left = target_node.left
        return root


if __name__ == "__main__":
    s = Solution()
    root = [5, 3, 6, 2, 4, None, 7]
    root = [3]
    root = initialTree(root)
    key = 3
    print(s.deleteNode(root, key))
