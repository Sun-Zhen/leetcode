# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/25
@version: 1.0.0.0
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res_node = temp_node = ListNode(0)
        flag = False
        while l1 is not None or l2 is not None or flag:
            temp_res = 0
            if flag:
                temp_res = 1
                flag = False
            if l1 is not None:
                temp_res += l1.val
            if l2 is not None:
                temp_res += l2.val
            if temp_res >= 10:
                flag = True
                temp_res = temp_res - 10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            temp_node.val = temp_res
            if l1 is not None or l2 is not None or flag:
                temp_node.next = ListNode(0)
                temp_node = temp_node.next
        return res_node


# (2 -> 4 -> 3) + (5 -> 6 -> 4)
if __name__ == "__main__":
    a = ListNode(3)
    b = ListNode(4)
    c = ListNode(2)
    c.next = b
    b.next = a
    x = ListNode(4)
    y = ListNode(6)
    z = ListNode(5)
    z.next = y
    y.next = x
    s = Solution()
    tmp = s.addTwoNumbers(c, z)
    while tmp is not None:
        print tmp.val
        tmp = tmp.next
