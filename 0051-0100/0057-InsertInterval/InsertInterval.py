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
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        插入到前面
        插入到中间不合并
        插入到中间合并
        插入到后面
        """
        if intervals is None or len(intervals) == 0:
            return [newInterval]
        result = list()
        for temp in range(len(intervals)):
            if intervals[temp].end < newInterval.start:
                result.append(intervals[temp])
            elif intervals[temp].start > newInterval.end:
                result.append(newInterval)
                result.extend(intervals[temp:])
                break
            else:
                newInterval.start = min(intervals[temp].start, newInterval.start)
                newInterval.end = max(intervals[temp].end, newInterval.end)
            if temp == len(intervals) - 1:
                result.append(newInterval)
        return result


if __name__ == "__main__":
    s = Solution()
    a = list()
    # [1, 2], [3, 5], [6, 7], [8, 10], [12, 16]
    # [1, 2], [3, 10], [12, 16].
    # a.append(Interval(1, 2))
    # a.append(Interval(3, 5))
    # a.append(Interval(6, 7))
    # a.append(Interval(8, 10))
    # a.append(Interval(12, 16))

    a.append(Interval(1, 5))
    b = Interval(6, 8)
    res = s.insert(a, b)
    for t in res:
        print t.start, t.end
