# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/1
@version: 1.0.0.0
"""


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if len(nums) == 1:
        #     return True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return self.check(nums[:i] + nums[i + 1:]) or self.check(
                    nums[:i + 1] + nums[i + 2:])
        return True

    def check(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print s.checkPossibility([4, 2, 3])
    print s.checkPossibility([1, 2, 3])
    print s.checkPossibility([4, 2, 1])
    print s.checkPossibility([3, 4, 2, 3])
    print s.checkPossibility([2, 2, 1, 2, 3])
    print s.checkPossibility([1])
