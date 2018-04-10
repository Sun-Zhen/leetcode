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
        temp_min = 0
        max_profit = 0
        for i in range(len(prices)):
            if i == 0:
                temp_min = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - temp_min)
            temp_min = min(temp_min, prices[i])
        return max_profit


if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([7, 1, 5, 3, 6, 4])
    print s.maxProfit([7, 6, 4, 3, 1])
    print s.maxProfit([])
