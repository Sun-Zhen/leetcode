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
        temp_dict = dict()
        for v in nums:
            temp_dict[v] = temp_dict.get(v, 0) + 1
        temp_max = 0
        for k, v in temp_dict.items():
            if k - 1 in temp_dict:
                temp_max = max(temp_max, v + temp_dict[k - 1])
            if k + 1 in temp_dict:
                temp_max = max(temp_max, v + temp_dict[k + 1])
        return temp_max


if __name__ == "__main__":
    s = Solution()
    print s.findLHS([1, 3, 2, 2, 5, 2, 3, 7])  # 5
    print s.findLHS([1, 1, 1, 1])  # 0
    print s.findLHS([1, 2, 3, 4])  # 2
