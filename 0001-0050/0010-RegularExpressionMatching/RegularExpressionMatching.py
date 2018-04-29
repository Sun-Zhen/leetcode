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
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1:
            return len(s) == 1 and (p[0] == "." or p[0] == s[0])
        if p[1] != "*":
            if len(s) == 0:
                return False
            return (s[0] == p[0] or p[0] == ".") and self.isMatch(s[1:], p[1:])
        while len(s) > 0 and (p[0] == s[0] or p[0] == "."):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
        return self.isMatch(s, p[2:])


if __name__ == "__main__":
    s = Solution()
    # print s.isMatch("aa", "a")  # false
    # print s.isMatch("aa", "aa")  # true
    # print s.isMatch("aaa", "aa")  # false
    # print s.isMatch("aa", "a*")  # true
    # print s.isMatch("aa", ".*")  # true
    # print s.isMatch("ab", ".*")  # true
    # print s.isMatch("aab", "c*a*b")  # true
    # print s.isMatch("mississippi", "mis*is*p*.")  # false
    # print s.isMatch("ab", ".*c")  # false
    # print s.isMatch("aaa", "ab*ac*a")  # true
    print s.isMatch("aaca", "ab*a*c*a")  # true
