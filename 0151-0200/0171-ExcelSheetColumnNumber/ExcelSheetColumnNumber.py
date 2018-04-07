# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_dict = dict()
        for n in range(65, 91):
            letter_dict.setdefault(chr(n), n - 64)
        res = 0
        for _, v in enumerate(s):
            res = res * 26 + letter_dict[v]
        return res


if __name__ == "__main__":
    s = Solution()
    print s.titleToNumber("A")
    print s.titleToNumber("B")
    print s.titleToNumber("AZ")
    print s.titleToNumber("BA")
    print s.titleToNumber("AA")
