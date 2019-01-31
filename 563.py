# coding: utf-8
""" 563. 二叉树的坡度

给定一个二叉树，计算整个树的坡度。
一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。
整个树的坡度就是其所有节点的坡度之和。

示例:

输入:
         1
       /   \
      2     3
输出: 1
解释:
结点的坡度 2 : 0
结点的坡度 3 : 0
结点的坡度 1 : |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1
"""
from tree_util import initialTree


class Solution:
    def __init__(self):
        self.result = list()

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.walkTree(root)
        return sum(self.result)

    def walkTree(self, s):
        """
        迭代实现
        :type s: TreeNode
        """
        if s is None:
            return 0
        left_sum = self.walkTree(s.left)
        right_sum = self.walkTree(s.right)
        s_node_value = abs(left_sum - right_sum)
        self.result.append(s_node_value)
        return s.val + left_sum + right_sum


if __name__ == '__main__':
    # l = [-8, 3, 0, -8, None, None, None, None, -1, None, 8]
    l = [1, 2, 3]
    tree = initialTree(l)
    s = Solution()
    print(s.findTilt(tree))
