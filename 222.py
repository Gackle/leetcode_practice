# coding: utf-8
""" 222. 完全二叉树的节点个数
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

思路：
0. 分别求节点的左子树深度（左子树的最左节点的深度）和右子树的深度（右子树的最左节点的深度）
1. 相等，右子树递归第 0 步操作
2. 左子树大于右子树，左子树递归第 0 步操作
3. 不存在左右子树，返回，得到的就是最后的叶子节点
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        # 每轮根节点的索引，初始为 0 
        index = 0
        current = root
        while current.left:
            # 求右子树深度
            right_depth = self.find_depth(current.right)
            # 求左子树深度
            left_depth = self.find_depth(current.left)
            # 对下一轮递归处理
            if right_depth == left_depth:
                current = current.right
                index = index * 2 + 2
            else:
                current = current.left
                index = index * 2 + 1
        return index + 1
    

    def find_depth(self, node):
        """
        :type node: TreeNode
        :rtype: int
        """
        depth = 0
        while node is not None:
            node = node.left
            depth += 1
        return depth


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
    tree = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    tree = []
    root = initialTree(tree)
    print(s.countNodes(root))
