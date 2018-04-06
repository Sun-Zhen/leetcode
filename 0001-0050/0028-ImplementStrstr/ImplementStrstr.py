# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0
        for i, v1 in enumerate(haystack):
            if len(haystack[i:]) < len(needle):
                return -1
            else:
                flag = True
                for j, v2 in enumerate(needle):
                    if v2 != haystack[i + j]:
                        flag = False
                        break
                if flag:
                    return i
        return -1


if __name__ == "__main__":
    s = Solution()
    print s.strStr("hello", "ll")
    print s.strStr("aaaaa", "bba")
    print s.strStr("", "")
    print s.strStr("", "a")
