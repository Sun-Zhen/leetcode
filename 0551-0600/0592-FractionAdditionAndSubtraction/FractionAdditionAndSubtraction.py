# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/18
@version: 1.0.0.0
"""


class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        a = b = None
        for i, v in enumerate(expression):
            pass


if __name__ == "__main__":
    s = Solution()
    print s.fractionAddition("-1/2+1/2")
    print s.fractionAddition("-1/2+1/2+1/3")
    print s.fractionAddition("1/3-1/2")
    print s.fractionAddition("5/3+1/3")
