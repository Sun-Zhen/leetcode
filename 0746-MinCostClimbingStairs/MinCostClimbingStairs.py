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
        print self.test(cost, 0, 0)

    def test(self, cost, index, sum_cost):
        if index >= len(cost):
            print index, sum_cost
            return sum_cost
        else:
            self.test(cost, index + 2, sum_cost + cost[index])
            self.test(cost, index + 1, sum_cost + cost[index])


if __name__ == "__main__":
    s = Solution()
    print s.minCostClimbingStairs([10, 15, 20])
    # print s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
