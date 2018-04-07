# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/31
@version: 1.0.0.0
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        min_cost = [None for _ in range(len(cost) + 1)]
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]
        for i in range(2, len(cost) + 1):
            if i != len(cost):
                min_cost[i] = min(min_cost[i - 2] + cost[i], min_cost[i - 1] + cost[i])
            else:
                min_cost[i] = min([min_cost[i - 2], min_cost[i - 1]])
        return min(min_cost[len(cost)], min_cost[len(cost) - 1])


if __name__ == "__main__":
    s = Solution()
    print s.minCostClimbingStairs([10, 15, 20])
    print s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
