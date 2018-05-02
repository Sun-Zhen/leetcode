# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()

        def dfs(t_list, t_nums):
            if len(t_nums) == 0:
                res.append(t_list)
            else:
                for i in range(len(t_nums)):
                    dfs(t_list + [t_nums[i]], t_nums[:i] + t_nums[i + 1:])

        dfs([], nums)
        return res


if __name__ == "__main__":
    s = Solution()
    print s.permute([1, 2, 3])
