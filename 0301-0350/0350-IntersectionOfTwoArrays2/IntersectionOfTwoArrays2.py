# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/14
@version: 1.0.0.0
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp_dict = dict()
        for _, v in enumerate(nums1):
            temp_dict[v] = temp_dict.get(v, 0) + 1
        res = list()
        for _, v in enumerate(nums2):
            if v in temp_dict and temp_dict[v] > 0:
                res.append(v)
                temp_dict[v] -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    print s.intersect([1, 2, 2, 1], [2, 2])
