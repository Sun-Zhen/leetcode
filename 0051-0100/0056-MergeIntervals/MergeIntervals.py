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
        基本思想都是先排序，再merge
        """
        if len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        result = list()
        target_interval = None
        for temp in range(len(intervals)):
            if temp == 0:
                target_interval = intervals[temp]
            else:
                if target_interval.end < intervals[temp].start:
                    result.append(target_interval)
                    target_interval = intervals[temp]
                else:
                    target_interval.start = min(target_interval.start, intervals[temp].start)
                    target_interval.end = max(target_interval.end, intervals[temp].end)
            if temp == len(intervals) - 1:
                result.append(target_interval)
        return result


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
        print t.start, t.end
