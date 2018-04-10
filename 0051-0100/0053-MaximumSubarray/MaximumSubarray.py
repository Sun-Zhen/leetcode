# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = list()
        for i in range(len(nums)):
            if i == 0:
                dp.append(nums[i])
            else:
                dp.append(max(dp[i - 1] + nums[i], nums[i]))
        return max(dp)


if __name__ == "__main__":
    s = Solution()
    print s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print s.maxSubArray([1])
    print s.maxSubArray([-2, -1])
