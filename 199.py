# -*- coding: utf-8 -*-
""" 199. 二叉樹的右視圖
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

思路：
深度遍歷 廣度遍歷
"""
from tree_util import initial_tree, TreeNode
from typing import List


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [(root, 0)]
        result = []
        layout = -1
        while queue:
            item = queue.pop(0)  # 出隊
            if item[1] != layout:
                layout = item[1]
                result.append(item[0].val)
            if item[0].right:
                queue.append((item[0].right, item[1]+1))
            if item[0].left:
                queue.append((item[0].left, item[1]+1))
        return result


if __name__ == "__main__":
    s = Solution()
    l = [1, 2, 3, None, 5, None, 4]  # [1, 3, 4]
    print(s.rightSideView(initial_tree(l)))
