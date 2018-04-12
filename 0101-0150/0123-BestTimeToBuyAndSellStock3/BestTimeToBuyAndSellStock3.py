# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[], []]
        temp_min = 0
        for i, v in enumerate(prices):
            if i == 0:
                temp_min = v
                dp[0][0] = 0
                dp[1][0] = 0
            else:
                if v > temp_min:
                    pass
                else:
                    pass
                temp_min = v if v < temp_min else temp_min
        return max(dp[0][-1], dp[1][-1])


if __name__ == "__main__":
    s = Solution()
    # print s.maxProfit()
