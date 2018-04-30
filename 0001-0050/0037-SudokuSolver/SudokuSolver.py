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
            if i > 8:
                return True
            if j > 8:
                return dfs(i + 1, 0)
            if board[i][j] == ".":
                for t in range(1, 10):
                    board[i][j] = chr(ord("0") + t)
                    if is_valid(i, j) and dfs(i, j + 1):
                        return True
                    else:
                        board[i][j] = "."
            else:
                return dfs(i, j + 1)
            return False

        def is_valid(i, j):
            # 规则1
            if board[i][j] in board[i][:j] + board[i][j + 1:]:
                return False
            # 规则2
            for t in range(9):
                if t != i and board[t][j] == board[i][j]:
                    return False
            # 规则3
            t_i, t_j, t_list = i / 3, j / 3, list()
            for x in range(3):
                for y in range(3):
                    if t_i * 3 + x != i and t_j * 3 + y != j:
                        t_list.append(board[t_i * 3 + x][t_j * 3 + y])
            if board[i][j] in t_list:
                return False
            return True

        dfs(0, 0)


if __name__ == "__main__":
    s = Solution()
    tmp = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s.solveSudoku(tmp)
