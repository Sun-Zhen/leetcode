# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/28
@version: 1.0.0.0
"""


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        if len(nums) >= 2:
            if nums[0] >= nums[1]:
                first_max = 0
                second_max = 1
            else:
                first_max = 1
                second_max = 0
            for tmp in range(2, len(nums)):
                if nums[tmp] > nums[first_max]:
                    second_max = first_max
                    first_max = tmp
                elif nums[second_max] < nums[tmp] < nums[first_max]:
                    second_max = tmp
            if nums[second_max] * 2 <= nums[first_max]:
                return first_max
            else:
                return -1


if __name__ == "__main__":
    s = Solution()
    print (s.dominantIndex([3, 6, 1, 0]))
    print (s.dominantIndex([1, 2, 3, 4]))
