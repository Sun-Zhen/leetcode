# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, v in enumerate(nums):
            if v <= 0:
                continue


if __name__ == "__main__":
    s = Solution()
    print s.firstMissingPositive([1, 2, 0])
    print s.firstMissingPositive([3, 4, -1, 1])
