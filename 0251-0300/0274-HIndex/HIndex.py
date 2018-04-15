# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/15
@version: 1.0.0.0
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations, reverse=True)
        temp_res = 0
        for i, v in enumerate(citations):
            if v >= i + 1:
                temp_res = i + 1
            else:
                break
        return temp_res


if __name__ == "__main__":
    s = Solution()
    print s.hIndex([3, 0, 6, 1, 5])
    print s.hIndex([0, 1])
