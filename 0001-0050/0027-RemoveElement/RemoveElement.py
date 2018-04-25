# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] != val:
                left += 1
            elif nums[right] == val:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        for _ in range(left, len(nums)):
            if nums[left] == val:
                del nums[left]
            else:
                left += 1
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    print s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    print s.removeElement([1], 1)
