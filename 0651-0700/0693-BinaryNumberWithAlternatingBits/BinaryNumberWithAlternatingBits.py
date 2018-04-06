# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/31
@version: 1.0.0.0
"""


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        str_num = bin(n)[2:]
        if len(str_num) == 1:
            return True
        else:
            for i in range(len(str_num) - 1):
                if str_num[i] == str_num[i + 1]:
                    return False
            return True


if __name__ == "__main__":
    s = Solution()
    print s.hasAlternatingBits(5)
    print s.hasAlternatingBits(7)
    print s.hasAlternatingBits(11)
    print s.hasAlternatingBits(10)
