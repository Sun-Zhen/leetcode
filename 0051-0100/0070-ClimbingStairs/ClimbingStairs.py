# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = list()
        dp.append(1)
        for i in range(1, n + 1):
            if i == 1:
                dp.append(1)
            else:
                dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print s.climbStairs(2)
    print s.climbStairs(3)
    print s.climbStairs(1)
    print s.climbStairs(5)
