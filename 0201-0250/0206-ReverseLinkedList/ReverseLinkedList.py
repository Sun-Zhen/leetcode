# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/23
@version: 1.0.0.0
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        next_node = None
        while head is not None:
            tmp = head.next
            head.next = next_node
            next_node = head
            head = tmp
        return next_node

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        [1, 2, 3, 4]
        x -> 1
        x -> 2 -> 1
        """
        if head is None:
            return None
        dummy_node = ListNode(0)
        dummy_node.next = head
        while head.next is not None:
            tmp = head.next
            head.next = tmp.next
            tmp.next = dummy_node.next
            dummy_node.next = tmp
        return dummy_node.next

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = head
        head = self.reverseList(p.next)
        p.next.next = p
        p.next = None
        return head


if __name__ == "__main__":
    pass
