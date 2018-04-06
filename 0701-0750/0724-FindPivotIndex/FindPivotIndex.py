# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/31
@version: 1.0.0.0
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 2:
            return -1
        elif len(nums) == 1:
            return 0
        else:
            all_sum = sum(nums)
            tmp_sum = 0
            res = -1
            for i in range(0, len(nums)):
                if i == 0:
                    tmp_sum = 0
                else:
                    tmp_sum += nums[i - 1]
                if tmp_sum == float(all_sum - nums[i]) / 2:
                    res = i
                    break
            return res


if __name__ == "__main__":
    s = Solution()
    print s.pivotIndex([1, 7, 3, 6, 5, 6])
    print s.pivotIndex([-1, -1, -1, -1, -1, -1])
    print s.pivotIndex([-1, -1, -1, 0, 1, 1])
    print s.pivotIndex([-1, -1, 0, 1, 1, 0])
