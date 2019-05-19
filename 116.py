# coding: utf-8
"""
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

提示：
深度优先遍历 (广度优先遍历/层次遍历)

思路：一开始的想法是 DFS ，后序遍历（右左中：主要是因为完美二叉树）递归用栈存下来每一层下一个的 next 的值，这样就会开到 （层数）* 1 个大小的栈；
discuss 区的第一个想法提醒了我，用右中左也可以实现同时减去了栈的开销
"""
import json


# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not (root and root.left):
            # 前提：完美二叉树
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root


def build_tree(tree: dict) -> Node:
    val = tree["val"]
    if "left" in tree and tree["left"]:
        left = build_tree(tree["left"])
    else:
        left = None
    if "right" in tree and tree["right"]:
        right = build_tree(tree["right"])
    else:
        right = None
    node = Node(val, left, right, None)
    return node


def print_tree(tree: Node) -> None:
    if tree.next:
        print(tree.val, "->", tree.next.val)
    if not tree.left:
        return
    else:
        print_tree(tree.left)
        print_tree(tree.right)
        return

if __name__ == "__main__":
    s = Solution()
    str_root = '{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}'
    str_root = 'null'
    dict_root = json.loads(str_root)
    root = build_tree(dict_root)
    root = s.connect(root)
    print_tree(root)
