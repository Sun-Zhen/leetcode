# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals is None:
            return None
        elif len(intervals) == 1:
            return intervals
        else:
            res = list()
            for i in range(len(intervals)):
                if i == 0:
                    pass


if __name__ == "__main__":
    # [1, 3], [2, 6], [8, 10], [15, 18],
    a = list()
    a.append(Interval(1, 3))
    a.append(Interval(2, 6))
    a.append(Interval(8, 10))
    a.append(Interval(15, 18))
    s = Solution()
    res = s.merge(a)
    for t in res:
        print t.s, t.e
