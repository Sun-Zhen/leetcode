# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/7
@version: 1.0.0.0
"""


class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """


if __name__ == "__main__":
    s = Solution()
    s.minSwap([1, 3, 5, 4],
              [1, 2, 3, 7])

    s.minSwap([0, 4, 4, 5, 9],
              [0, 1, 6, 8, 10])

    s.minSwap([2, 3, 2, 5, 6],
              [0, 1, 4, 4, 5])
