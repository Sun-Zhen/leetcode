# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/25
@version: 1.0.0.0
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        s的长度最长为1000
        """
        dp = [[True if i == j else False for j in s] for i in s]
        for i, vi in enumerate(s):
            for j, vj in enumerate(s):
                pass


if __name__ == "__main__":
    s = Solution()
    print s.longestPalindrome("babad")
    print s.longestPalindrome("cbbd")
