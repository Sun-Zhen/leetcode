# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/29
@version: 1.0.0.0
"""


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.dp = [[None for _ in range(len(nums))] for _ in range(len(nums))]
        for t1 in range(len(self.nums)):
            for t2 in range(t1, len(self.nums)):
                if t1 == t2:
                    self.dp[t1][t2] = nums[t2]
                else:
                    self.dp[t1][t2] = self.dp[t1][t2 - 1] + nums[t2]
                    
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0:
            i = 0
        if j >= len(self.nums):
            j = len(self.nums) - 1
        return self.dp[i][j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


if __name__ == "__main__":
    n = NumArray([-2, 0, 3, -5, 2, -1])
    print n.sumRange(0, 2)
    print n.sumRange(2, 5)
    print n.sumRange(0, 5)
