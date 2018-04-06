# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp = list()
        test = head
        while test is not None:
            tmp.append(test)
            test = test.next
        index = len(tmp) - n
        if index == 0:
            return head.next
        elif index == len(tmp) - 1:
            tmp[index - 1].next = None
            return head
        else:
            tmp[index - 1].next = tmp[index + 1]
            return head


if __name__ == "__main__":
    head = temp = ListNode(1)
    temp.next = ListNode(2)
    temp = temp.next
    temp.next = ListNode(3)
    temp = temp.next
    temp.next = ListNode(4)
    temp = temp.next
    temp.next = ListNode(5)
    s = Solution()
    head = s.removeNthFromEnd(head, 2)
    temp = head
    while temp is not None:
        print temp.val
        temp = temp.next
