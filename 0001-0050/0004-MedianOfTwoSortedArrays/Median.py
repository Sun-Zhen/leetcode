# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/25
@version: 1.0.0.0
"""


class Solution(object):
    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums = sorted(nums1)
        length = len(nums)
        if length == 0:
            return list()
        elif length == 1:
            return nums[0]
        if length % 2 == 0:
            return float(nums[length / 2 - 1] + nums[length / 2]) / 2
        else:
            return nums[length / 2]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


if __name__ == "__main__":
    s = Solution()
    print s.findMedianSortedArrays([1, 2], [3, 4])
