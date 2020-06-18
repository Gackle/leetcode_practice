# -*- conding: utf-8 -*-
""" 56. 合并区间
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""
from typing import List
from tree_util import initial_tree, TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        if not root:
            return result

        def dfs(node: TreeNode, path: str = ""):
            path += str(node.val)
            if node.left is None and node.right is None:
                result.append(path)
            else:
                path += "->"
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)

        dfs(root)

        return result


if __name__ == "__main__":
    s = Solution()
    # l = [1, 2, 3, None, 5]
    l = [1]
    root = initial_tree(l)
    print(s.binaryTreePaths(root))
