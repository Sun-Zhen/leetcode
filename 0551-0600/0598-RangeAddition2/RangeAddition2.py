# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/18
@version: 1.0.0.0
"""


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops is None or len(ops) == 0:
            return m * n
        x_min = ops[0][0]
        y_min = ops[0][1]
        for tmp_ops in ops:
            x_min = tmp_ops[0] if tmp_ops[0] < x_min else x_min
            y_min = tmp_ops[1] if tmp_ops[1] < y_min else y_min
        return x_min * y_min


if __name__ == "__main__":
    s = Solution()
    print s.maxCount(3, 3, [[2, 2], [3, 3]])
    print s.maxCount(3, 3, [])
