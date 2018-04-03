# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/31
@version: 1.0.0.0
"""


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        letter_dict = dict()
        letter_len_dict = dict()
        for tmp in range(len(nums)):
            letter_dict.setdefault(nums[tmp], []).append(tmp)
            letter_len_dict[nums[tmp]] = len(letter_dict[nums[tmp]])
        max_degree = max(letter_len_dict.values())
        min_list = list()
        for k, v in letter_dict.items():
            if len(v) == max_degree:
                min_list.append(max(v) - min(v) + 1)
        return min(min_list)


if __name__ == "__main__":
    s = Solution()
    print s.findShortestSubArray([1, 2, 2, 3, 1])
    print s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2])
