# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = tmp = ListNode()
        while head is not None:
            pass
        return res.next


if __name__ == "__main__":
    head1 = temp = ListNode(5)
    temp.next = ListNode(6)
    temp = temp.next
    temp.next = ListNode(4)
    temp = temp.next
    temp.next = ListNode(1)
    temp = temp.next
    temp.next = ListNode(2)
    s = Solution()
    res1 = s.sortList(head1)
    while res1 is not None:
        print res1.val
        res1 = res1.next
