# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/29
@version: 1.0.0.0
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
if __name__ == "__main__":
    L1 = ListNode(1)
    L1.next = ListNode(2)
    L1.next.next = ListNode(4)
    L2 = ListNode(1)
    L2.next = ListNode(3)
    L2.next.next = ListNode(4)
    s = Solution()
    s.mergeTwoLists(L1, L2)
