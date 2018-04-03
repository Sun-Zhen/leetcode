# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/28
@version: 1.0.0.0
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        reverse = 0
        while x > reverse:
            if x / 10 == reverse:
                return True
            reverse = 10 * reverse + x % 10
            x = x / 10
        if x == reverse:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome(123321)
    print s.isPalindrome(12421)
    print s.isPalindrome(10)
