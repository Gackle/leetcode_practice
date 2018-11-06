# coding: utf-8
""" 671. 二叉树中第二小的节点

给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。 
给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

示例 1:
输入:
    2
   / \
  2   5
     / \
    5   7
输出: 5
说明: 最小的值是 2 ，第二小的值是 5 。

示例 2:
输入:
    2
   / \
  2   2
输出: -1
说明: 最小的值是 2, 但是不存在第二小的值。

思路：由树的性质可以确定了这根节点基本上就是最小的节点了，而第二小的节点是否存在，取决于根的左右节点 —— 如果左右节点均和根节点相等，则没有；
否则，在相同的左或右节点往下找到不同的值则为第二小节点，如果都相同，则不同的根的左（或右）节点为第二小节点，严格意义上来说是递归的实现
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None or (root.left is None and root.right is None):
            return -1
        l, r = -1, -1
        if root.left:
            l = root.left.val if root.val != root.left.val else self.findSecondMinimumValue(
                root.left)
        if root.right:
            r = root.right.val if root.val != root.right.val else self.findSecondMinimumValue(
                root.right)
        if l == -1:
            return r
        elif r == -1:
            return l
        else:
            return min(l, r)


def initialTree(li):
    '''
    :type li: List[int]
    '''
    if not li:
        return None
    root = buildTree(TreeNode(li[0]), 0, li)
    return root


def buildTree(parent, i, li):
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


if __name__ == '__main__':
    tree = [2, 2, 5, None, None, 5, 7]
    # tree = [1, 1, 3, 1, 1, 3, 4, 3, 1, 1, 1, 3, 8, 4, 8, 3, 3, 1, 6, 2, 1]
    s = Solution()
    root = initialTree(tree)
    print(s.findSecondMinimumValue(root))
