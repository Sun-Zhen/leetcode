# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


if __name__ == "__main__":
    s = Solution()
    r = s.permuteUnique([1, 1, 2])
    for _, v in enumerate(r):
        print v
