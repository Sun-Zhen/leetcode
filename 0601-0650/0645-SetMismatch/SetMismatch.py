# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/2
@version: 1.0.0.0
"""


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            temp[nums[i] - 1] += 1
        res = [-1, -1]
        for i in range(len(nums)):
            if temp[i] == 2:
                res[0] = i + 1
            if temp[i] == 0:
                res[1] = i + 1
            if res[0] != -1 and res[1] != -1:
                break
        return res


if __name__ == "__main__":
    s = Solution()
    print s.findErrorNums([1, 2, 2, 4])
    print s.findErrorNums([4, 1, 2, 2])
