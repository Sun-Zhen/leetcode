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
        res = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                res += (prices[i + 1] - prices[i])
        return res


if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([1, 2])
