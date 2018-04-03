# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/1
@version: 1.0.0.0
"""


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
        dx = dy = [-1, 0, 1]
        for i in range(len(M)):
            for j in range(len(M[0])):
                print i, j, len(M), len(M[0])
                temp_list = list()
                [temp_list.append(M[i + x][j + y]) for x in dx for y in dy if
                 0 <= i + x < len(M) and 0 <= j + y < len(M[0])]
                print temp_list
                res[i][j] = sum(temp_list) / len(temp_list)
        return res


if __name__ == "__main__":
    s = Solution()
    # print s.imageSmoother([[1, 1, 1],
    #                        [1, 0, 1],
    #                        [1, 1, 1]])
    print s.imageSmoother([[2, 3, 4],
                           [5, 6, 7],
                           [8, 9, 10],
                           [11, 12, 13],
                           [14, 15, 16]])
