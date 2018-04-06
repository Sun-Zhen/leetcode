# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = None
        i = 0
        while i != len(nums):
            if i == 0:
                temp = nums[i]
            elif temp == nums[i]:
                del nums[i]
                i -= 1
            else:
                temp = nums[i]
            i += 1
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    print s.removeDuplicates([1, 1, 2])
    print s.removeDuplicates([1, 1, 1])
