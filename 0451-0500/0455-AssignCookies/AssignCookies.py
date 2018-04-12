# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/12
@version: 1.0.0.0
"""


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        res = 0
        for t1 in s:
            for t2 in g[res:]:
                if t1 >= t2:
                    res += 1
                    break
        return res


if __name__ == "__main__":
    s = Solution()
    print s.findContentChildren([1, 2, 3], [1, 1])
