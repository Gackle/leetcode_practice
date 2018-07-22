# coding: utf-8
''' 94. 二叉树的中序遍历
'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.return_list = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is not None:
            self.inorderTraversal(root.left)
            self.return_list.append(root.val)
            self.inorderTraversal(root.right)

        return self.return_list


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


if __name__ == '__main__':
    li = [1, None, 2, 3]
    root = initialTree(li)
    s = Solution()
    print(s.inorderTraversal(root))
