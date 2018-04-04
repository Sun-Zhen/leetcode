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
        start = 0
        target = None
        for i1, v1 in enumerate(p):
            if v1 == ".":
                target = s[start]
                start += 1
            elif v1 == "*":
                if i1 - 1 >= 0:
                    if p[i1 - 1] != ".":
                        target = p[i1 - 1]
                    while start < len(s) and s[start] == target:
                        start += 1
                else:
                    continue
            else:
                if s[start] == v1:
                    start += 1
                else:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    print s.isMatch("aa", "a")  # false
    print s.isMatch("aa", "aa")  # true
    print s.isMatch("aaa", "aa")  # false
    print s.isMatch("aa", "a*")  # true
    print s.isMatch("aa", ".*")  # true
    print s.isMatch("ab", ".*")  # true
    print s.isMatch("aab", "c*a*b")  # true
