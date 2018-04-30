# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = list()
        candidates = sorted(candidates)

        def dfs(t_sum, t_list, index):
            if t_sum > target:
                return False
            elif t_sum == target:
                res.append(t_list)
            else:
                for i in range(index, len(candidates)):
                    dfs(t_sum + candidates[i], t_list + [candidates[i]], i)

        dfs(0, [], 0)
        return res


if __name__ == "__main__":
    s = Solution()
    print s.combinationSum([2, 3, 6, 7], 7)
    print s.combinationSum([2, 3, 5], 8)
