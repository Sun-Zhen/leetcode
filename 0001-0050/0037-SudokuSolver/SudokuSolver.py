# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        检查每行，检查每列
        """

        def dfs(i, j):
            if i != 8 and j == 8:
                return

        dfs(0, 0)


if __name__ == "__main__":
    s = Solution()
    s.solveSudoku(None)
