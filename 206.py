# coding: utf-8
""" 206. 反转链表

反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        # 迭代求法
        self.reverse_iter(head)
        return self.head

    def reverse_iter(self, node):
        """
        :type node: ListNode
        :rtype: ListNode
        """
        if not node.next:
            self.head = node
            return node
        else:
            parent = self.reverse_iter(node.next)
            parent.next = ListNode(node.val)
            parent = parent.next
            return parent


class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        self.head = None
        # 递归求法
        self.reverse_recur(head)
        return self.head

    def reverse_recur(self, node):
        """
        :type node: ListNode
        :rtype: ListNode
        """
        if not node:
            return
        head = ListNode(node.val)
        head.next = self.head
        self.head = head
        self.reverse_recur(node.next)


def initListNode(li):
    """
    :type li: List
    :rtype: ListNode
    """
    if not li:
        return None
    root = ListNode(li[0])
    cur = root
    for i in li[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return root


if __name__ == '__main__':
    s = Solution2()
    li = [1, 2, 3, 4, 5]
    list_node = initListNode(li)
    t = s.reverseList(list_node)
    while t:
        print(t.val)
        t = t.next
