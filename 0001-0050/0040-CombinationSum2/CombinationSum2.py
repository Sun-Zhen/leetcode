# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
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
                    if i > index and candidates[i] == candidates[i - 1]:
                        continue
                    dfs(t_sum + candidates[i], t_list + [candidates[i]], i + 1)

        dfs(0, [], 0)
        return res


if __name__ == "__main__":
    s = Solution()
    print s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    # print s.combinationSum2([2, 5, 2, 1, 2], 5)
