# coding: utf-8
''' 538. 把二叉搜索树转换为累加树

给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，
使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：
输入: 二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

思路：从二叉搜索树特性入手 —— 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉搜索树。
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


def initialTree(li):
    '''
    :type li: List[int]
    '''
    if not li:
        return None
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
    s = Solution()
    li = [5, 2, 13, None, None, 10, 16, 7, 12]
    tree = initialTree(li)
    print(s.convertBST(tree))
