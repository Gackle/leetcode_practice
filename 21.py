# coding: utf-8
''' 21. 有序链表合并
'''


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        b = ListNode(0)
        b.next = self
        while b:
            b = b.next
            print(b.val, end=" ")
        # else:
        #     print(b.val, end="\n")


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l1
        tail = l2
        data = ListNode(0)
        tip = data
        while head and tail:
            if head.val <= tail.val:
                data.next = ListNode(head.val)
                head = head.next
            else:
                data.next = ListNode(tail.val)
                tail = tail.next
            data = data.next

        if not head:
            data.next = tail
        elif not tail:
            data.next = head

        return tip.next


if __name__ == '__main__':
    s = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(4)

    b = ListNode(1)
    b.next = ListNode(3)
    b.next.next = ListNode(4)
    b.next.next.next = ListNode(9)
    print(s.mergeTwoLists(a, b))
