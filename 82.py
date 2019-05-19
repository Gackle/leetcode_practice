# coding: utf-8
""" 82. 删除排序链表中的重复元素 II
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{} - {}".format(self.val, self.next is not None)


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """ 三指针法
        """
        if not head or not head.next:
            return head
        root = ListNode('a')
        root.next = head
        pre = root
        cur = pre.next
        while cur is not None:
            if cur.next and cur.next.val != cur.val or not cur.next:
                pre = cur
                cur = cur.next
            else:
                cp = cur.val
                tail = cur.next
                while tail is not None and tail.val == cp:
                    tail = tail.next
                pre.next = tail
                if tail is None:
                    break
                else:
                    cur = tail
        return root.next


if __name__ == "__main__":
    s = Solution()
    l = [1, 2, 3, 3, 4, 4, 5]
    l = [1, 1, 2, 3]
    l = [1, 1]
    root = ListNode(-1)
    p = root
    for i in l:
        p.next = ListNode(i)
        p = p.next
    root = root.next
    r = s.deleteDuplicates(root)
    while r is not None:
        print(r.val, end="\t")
        r = r.next
