# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/27
@version: 1.0.0.0
"""


class Solution(object):
    def numberOfLines(self, widths, S):
        """
        时间复杂度O(n)
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = {1: 0}
        for tmp in S:
            lines[len(lines)] += widths[ord(tmp) - 97]
            if lines[len(lines)] > 100:
                lines[len(lines)] -= widths[ord(tmp) - 97]
                lines[len(lines) + 1] = widths[ord(tmp) - 97]
        return [len(lines), lines[len(lines)]]


if __name__ == "__main__":
    s = Solution()
    width_array = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                   10, 10, 10, 10, 10, 10]
    print (s.numberOfLines(width_array, "bbbcccdddaaa"))
