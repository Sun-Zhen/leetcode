# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        idx = distance = 0
        cur = nums[0]
        for _ in range(length):
            idx = (idx + k) % length
            nums[idx], cur = cur, nums[idx]
            distance = (distance + k) % length
            if distance == 0:
                idx = (idx + 1) % length
                cur = nums[idx]


if __name__ == "__main__":
    s = Solution()
    # s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
    # s.rotate([1, 2, 3, 4, 5, 6], 2)
    # s.rotate([1], 0)
    # s.rotate([1], 1)
    s.rotate([1, 2, 3, 4, 5, 6], 3)
