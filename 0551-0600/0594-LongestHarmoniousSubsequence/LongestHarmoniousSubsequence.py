# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/18
@version: 1.0.0.0
"""


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_max_dict = dict()  # 比当前key大1
        len_min_dict = dict()
        check_list = list()
        if nums is None or len(nums) == 0:
            return 0
        for i, v in enumerate(nums):
            if v in len_max_dict:
                len_max_dict[v] += 1
            else:
                len_max_dict[v] = 1
            if v + 1 in len_max_dict:
                len_max_dict[v + 1] += 1
                check_list.extend([v, v + 1])

            if v in len_min_dict:
                len_min_dict[v] += 1
            else:
                len_min_dict[v] = 1
            if v - 1 in len_min_dict:
                len_min_dict[v - 1] += 1
                check_list.extend([v, v - 1])
        temp_max = 0
        for _, v in enumerate(check_list):
            temp_max = max(temp_max, len_max_dict[v])
            temp_max = max(temp_max, len_min_dict[v])
        return temp_max


if __name__ == "__main__":
    s = Solution()
    print s.findLHS([1, 3, 2, 2, 5, 2, 3, 7])  # 5
    print s.findLHS([1, 1, 1, 1])  # 0
    print s.findLHS([1, 2, 3, 4])  # 2
