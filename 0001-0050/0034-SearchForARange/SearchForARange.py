# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target < nums[0]:
            return [-1, -1]
        elif target > nums[len(nums) - 1]:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        pass


if __name__ == "__main__":
    s = Solution()
    print s.searchRange([5, 7, 7, 8, 8, 10], 8)
