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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        flag = 0
        last_one = None
        next_one = None
        last_two = None
        if head is None or head.next is None:
            return head
        else:
            res.next = head.next
        while head is not None:
            next_one = head.next
            flag += 1
            if flag % 2 == 0:
                head.next = last_one
                last_one.next = next_one
                if last_two is not None:
                    last_two.next = head
                last_two = last_one
                head = next_one
                continue
            last_one = head
            head = head.next
        return res.next


# 1->2->3->4
# 2->1->4->3
if __name__ == "__main__":
    head1 = temp = ListNode(1)
    temp.next = ListNode(2)
    temp = temp.next
    temp.next = ListNode(3)
    temp = temp.next
    temp.next = ListNode(4)
    s = Solution()
    res1 = s.swapPairs(head1)
    while res1 is not None:
        print res1.val
        res1 = res1.next
