# coding: utf-8
''' 100. 相同的树
'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None:
            return q is None
        if q is None:
            return p is None
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    ta = TreeNode(1)
    ta.right = TreeNode(2)
    tb = TreeNode(1)
    tb.left = TreeNode(2)
    s = Solution()
    print(s.isSameTree(ta, tb))
