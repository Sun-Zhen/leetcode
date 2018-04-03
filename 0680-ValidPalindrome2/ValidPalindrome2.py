# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/1
@version: 1.0.0.0
"""


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # for tmp_index in index_list:
        #     tmp_s = s[:tmp_index] + s[tmp_index + 1:]
        #     flag = True
        #     for i in range(len(tmp_s)):
        #         if tmp_s[i] != tmp_s[len(tmp_s) - 1 - i]:
        #             flag = False
        #             break
        #     if flag:
        #         return True
        # return False


if __name__ == "__main__":
    s = Solution()
    print s.validPalindrome("aba")
    print s.validPalindrome("abca")
    print s.validPalindrome("abc")
    print s.validPalindrome("deeee")
    print s.validPalindrome("eedede")
    print s.validPalindrome("cxcaac")
