# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [None for _ in range(len(nums))]
        dp[0] = 0


if __name__ == "__main__":
    s = Solution()
    print s.maxProduct([2, 3, -2, 4])  # 6
