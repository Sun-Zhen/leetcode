# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/4
@version: 1.0.0.0
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        '.' 匹配任意单个字符。
        '*' 匹配零个或多个前面的元素。
        """
        i = j = 0
        while i < len(s) and j < len(p):
            if j == 0:
                if p[0] == ".":
                    pass
                elif p[0] == "*":
                    pass
                else:
                    pass


if __name__ == "__main__":
    s = Solution()
    print s.isMatch("aa", "a")  # false
    print s.isMatch("aa", "aa")  # true
    print s.isMatch("aaa", "aa")  # false
    print s.isMatch("aa", "a*")  # true
    print s.isMatch("aa", ".*")  # true
    print s.isMatch("ab", ".*")  # true
    print s.isMatch("aab", "c*a*b")  # true
