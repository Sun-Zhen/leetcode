# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = -1
        for i, v in enumerate(nums):
            if target == v:
                return i
            elif v < target:
                res = i
        return res + 1


if __name__ == "__main__":
    s = Solution()
    print s.searchInsert([1, 3, 5, 6], 5)
    print s.searchInsert([1, 3, 5, 6], 2)
    print s.searchInsert([1, 3, 5, 6], 7)
    print s.searchInsert([1, 3, 5, 6], 0)
