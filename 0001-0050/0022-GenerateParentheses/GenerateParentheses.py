# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = list()

        def dfs(t_str, i, j):
            if i == 0 and j == 0:
                res.append(t_str)
            if i > 0:
                dfs(t_str + "(", i - 1, j)
            if j > i:
                dfs(t_str + ")", i, j - 1)

        dfs("", n, n)
        return res


if __name__ == "__main__":
    s = Solution()
    print s.generateParenthesis(3)
