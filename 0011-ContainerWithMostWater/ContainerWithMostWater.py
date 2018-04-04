# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/4
@version: 1.0.0.0
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        maxArea = 0
        for i, v in enumerate(height):
            if i == start:
                continue
            else:
                pass


if __name__ == "__main__":
    s = Solution()
    s.maxArea([1, 2, 3, 4])
