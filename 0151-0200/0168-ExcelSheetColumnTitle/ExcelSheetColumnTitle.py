# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while n:
            ans = chr(ord('A') + (n - 1) % 26) + ans
            n = (n - 1) / 26
        return ans


if __name__ == "__main__":
    s = Solution()
    print s.convertToTitle(26)
    print s.convertToTitle(27)
    print s.convertToTitle(28)
