# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/14
@version: 1.0.0.0
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp_dict = dict()
        for _, v in enumerate(nums1):
            temp_dict[v] = 1
        for _, v in enumerate(nums2):
            if v in temp_dict:
                temp_dict[v] = 2
        res = list()
        for k, v in temp_dict.items():
            if v == 2:
                res.append(k)
        return res


if __name__ == "__main__":
    s = Solution()
    print s.intersection([1, 2, 2, 1], [2, 2])
