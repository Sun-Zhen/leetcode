# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/29
@version: 1.0.0.0
"""


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        for i in range(len(self.nums)):
            pass

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0:
            i = 0
        if j >= len(self.nums):
            j = len(self.nums) - 1
        res = sum(self.nums[i, j + 1])
        return res


if __name__ == "__main__":
    n = NumArray([-2, 0, 3, -5, 2, -1])
    print n.sumRange(0, 2)
    print n.sumRange(2, 5)
    print n.sumRange(0, 5)
