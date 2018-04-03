# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/28
@version: 1.0.0.0
"""


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for x in range(0, len(matrix)):
            for y in range(0, len(matrix[x])):
                if matrix[x][y] == (matrix[x - 1][y - 1] if x >= 1 and y >= 1 else matrix[x][y]):
                    continue
                else:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    print (s.isToeplitzMatrix([[0]]))
    # 1,2
    # 2,2
