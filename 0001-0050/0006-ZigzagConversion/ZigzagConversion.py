# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/3
@version: 1.0.0.0
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        zigzag = ["" for _ in range(numRows)]
        print "".join(zigzag)
        row, step = 0, 1
        for c in s:
            zigzag[row] += c
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return "".join(zigzag)


if __name__ == "__main__":
    s = Solution()
    print s.convert("PAYPALISHIRING", 3)
