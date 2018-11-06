# coding: utf-8
""" 86. 分隔链表
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

!你应当保留两个分区中每个节点的初始相对位置。

示例:
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

思路：双指针
之前一开始的思路是，头插入和尾插入同时操作一个链表，发现情况太多难以控制
后面换一种思路，如果直接把它拆成两个链表做尾插入，再合并，就简单多了。果然加班加多了人都傻了
"""


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        # 前半部分游标
        h = ListNode(0)
        # 前半部分起始位置
        ph = h
        # 后半部分游标
        t = ListNode(0)
        # 后半部分起始位置
        pt = t
        while head:
            if head.val >= x:
                t.next = ListNode(head.val)
                t = t.next
            else:
                h.next = ListNode(head.val)
                h = h.next
            head = head.next
        h.next = pt.next
        return ph.next


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
    s = Solution()
    # link = [1, 4, 3, 2, 5, 2]
    # x = 5
    link = [2, 1]
    x = 2
    node = initListNode(link)
    r = s.partition(node, x)
    while r:
        print(r.val)
        r = r.next
