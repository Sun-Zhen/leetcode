# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        elif len(nums) == 1:
            return True
        temp_max = 0
        for i in range(len(nums) - 1):
            temp_max = max(temp_max, i + nums[i])
            if temp_max < i + 1:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print s.canJump([2, 3, 1, 1, 4])  # True
    print s.canJump([3, 2, 1, 0, 4])  # False
    print s.canJump([2, 5, 0, 0])  # True
