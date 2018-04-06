# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        不相邻元素的子数组sum值的最大值
        """
        size = len(nums)
        dp = [0] * (size + 1)
        if size:
            dp[1] = nums[0]
        for i in range(2, size + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[size]


if __name__ == "__main__":
    s = Solution()
    print s.rob([1, 4, 5, 6, 2, 3, 4])
