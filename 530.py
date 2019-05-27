# coding: utf-8
""" 530. 二叉搜索树的最小绝对差

给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。

示例 :
输入:
   1
    \
     3
    /
   2
输出:
1

解释:
最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。

思路：
利用 BST 的特性，当前节点的节点最小值，必定出现在 (node, node 左子树的最右节点) 和 
(node, node 右子树的最右节点之间)

思路二：
BST 的中序遍历为升序数组
"""
from tree_util import TreeNode, initialTree


class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        res = 99999999
        l = inorder(root)
        # print l
        for i in range(1, len(l)):
            res = min(res, l[i] - l[i - 1])

        return res


if __name__ == "__main__":
    s = Solution()
    li = [236, 104, 701, None, 227, None, 911]
    # li = [1, None, 3, 2]
    # li = [0, None, 2236, 1277, 2776, 519]
    root = initialTree(li)
    # root = TreeNode(0)
    # root.right = TreeNode(2236)
    # root.right.left = TreeNode(1277)
    # root.right.left.left = TreeNode(519)
    # root.right.right = TreeNode(2776)
    print(s.getMinimumDifference(root))
