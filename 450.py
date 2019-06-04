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

思路：(果然题目越长越简单)
二叉搜索树的性质
当找到对应节点的时候，如果左右根有一个为叶节点，则直接补上去；否则，补上右子树的最左节点
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_util import initial_tree, TreeNode


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        def merge(node: TreeNode):
            if not node.right:
                return node.left
            p = node.right
            while p.left:
                p = p.left
            p.left = node.left
            return node.right

        def search(node: TreeNode, parent: TreeNode, t: int, root: TreeNode):
            if node.val == key:
                # merge
                ne = merge(node)
                if node == root:
                    root = ne
                else:
                    if t == 1:
                        parent.left = ne
                    else:
                        parent.right = ne
            elif not node.left and not node.right:
                return root
            elif node.val < key and node.right:
                return search(node.right, node, 2, root)
            elif node.val > key and node.left:
                return search(node.left, node, 1, root)
            return root

        root = search(root, None, 0, root)
        return root

if __name__ == "__main__":
    s = Solution()
    root = [5, 3, 6, 2, 4, None, 7]
    # root = []
    # root = [3]
    root = initial_tree(root)
    key = 3
    print(s.deleteNode(root, key))
