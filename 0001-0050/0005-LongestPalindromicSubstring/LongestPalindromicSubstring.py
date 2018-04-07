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
        c = 0
        max_len = 0
        for i, v1 in enumerate(s):
            for j in range(i):
                pass


if __name__ == "__main__":
    s = Solution()
    print s.longestPalindrome("babad")
    print s.longestPalindrome("cbbd")
