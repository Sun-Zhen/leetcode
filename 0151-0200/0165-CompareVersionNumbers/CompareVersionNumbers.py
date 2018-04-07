# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        res1 = 0
        for i in range(len(v1)):
            if int(v1[i]) != 0:
                res1 = res1 * 10 + int(v1[i])
        res2 = 0
        for i in range(len(v2)):
            if int(v2[i]) != 0:
                res2 = res2 * 10 + int(v2[i])
        if res1 == res2:
            return 0
        else:
            return 1 if res1 > res2 else -1


if __name__ == "__main__":
    s = Solution()
    print s.compareVersion("0.1", "1.1")
    print s.compareVersion("1.1", "1.2")
    print s.compareVersion("1.2", "13.37")
    print s.compareVersion("13.222", "13.37")
    print s.compareVersion("01", "1")
    print s.compareVersion("0.1", "0.0.1")
    print s.compareVersion("1", "1.1")
    print s.compareVersion("1.0", "1")
    print s.compareVersion("1.0.0", "1")
