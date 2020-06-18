# -*- coding: utf-8 -*-
""" 1028. 从先序遍历还原二叉树
我们从二叉树的根节点 root 开始进行深度优先搜索。
在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。
（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。
如果节点只有一个子节点，那么保证该子节点为左子节点。
给出遍历输出 S，还原树并返回其根节点 root。

示例 1：
输入："1-2--3--4-5--6--7"
输出：[1,2,5,3,4,6,7]

示例 2：
输入："1-2--3---4-5--6---7"
输出：[1,2,5,3,null,6,null,4,null,7]

示例 3：
输入："1-401--349---90--88"
输出：[1,401,null,349,88,90]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_util import TreeNode, output_tree


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if S == "":
            return None
        depth = 0
        stack = []
        i = 0
        num = ""
        while i < len(S):
            if S[i] != "-":
                num += S[i]
            else:
                if num:
                    stack.append((depth, TreeNode(int(num))))
                    depth = 0
                    num = ""
                depth += 1
            i += 1
        stack.append((depth, TreeNode(int(num))))
        # 全部入栈之后，出栈
        right_stack = []
        while len(stack) > 1:
            p = stack.pop()
            if p[0] <= stack[-1][0]:
                # 为右节点
                right_stack.append(p)
                continue
            # 为左节点
            stack[-1][1].left = p[1]
            # 判断是否有适合的右节点
            if right_stack and stack[-1][0] == right_stack[-1][0] - 1:
                rp = right_stack.pop()
                stack[-1][1].right = rp[1]
        return stack[0][1]


if __name__ == "__main__":
    null = 'null'
    s = Solution()
    S = "1-2--3--4-5--6--7"
    assert output_tree(s.recoverFromPreorder(S)) == [1, 2, 5, 3, 4, 6, 7], output_tree(s.recoverFromPreorder(S))
    S = "1-2--3---4-5--6---7"
    assert output_tree(s.recoverFromPreorder(S)) == [
        1, 2, 5, 3, null, 6, null, 4, null, 7], output_tree(s.recoverFromPreorder(S))
    S = "1-401--349---90--88"
    assert output_tree(s.recoverFromPreorder(S)) == [1, 401, 'null', 349, 88, 90], output_tree(s.recoverFromPreorder(S))
