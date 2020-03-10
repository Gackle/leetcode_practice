# coding: utf-8
""" 543. 二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。

思路：计算左右两边的最大深度和 - 1
"""
from tree_util import TreeNode, initial_tree


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter

    def dfs(self, node: TreeNode) -> int:
        if node is None or not node.left and not node.right:
            return 0
        left_depth = self.dfs(node.left) + 1 if node.left else 0
        right_depth = self.dfs(node.right) + 1 if node.right else 0
        self.diameter = max(self.diameter, left_depth + right_depth)
        return max(left_depth, right_depth)


if __name__ == "__main__":
    s = Solution()
    # li = [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6,
    #       None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2]
    li = [1, 0, 0, 0, 0]
    root = initial_tree(li)
    print(s.diameterOfBinaryTree(root))
