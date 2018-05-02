# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/29
@version: 1.0.0.0
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """


if __name__ == "__main__":
    s = Solution()
    # print s.isMatch("aa", "a")  # false
    # print s.isMatch("aa", "*")  # true
    # print s.isMatch("cd", "?a")  # false
    # print s.isMatch("adceb", "*a*b")  # true
    # print s.isMatch("acdcb", "a*c?b")  # false
    # print s.isMatch("abefcdgiescdfimde", "ab*cd?i*de")  # true
    # print s.isMatch("aaaa", "***a")  # true
    # print s.isMatch("", "*")  # true
    # print s.isMatch("c", "*?*")  # true
    # print s.isMatch("hi", "*?")  # true
    print s.isMatch(
        "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
        , "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a")
    # print s.isMatch(
    #     "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
    #     , "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a")
