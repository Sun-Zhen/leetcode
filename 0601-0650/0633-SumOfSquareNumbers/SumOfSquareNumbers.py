# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/2
@version: 1.0.0.0
"""


# 1  2
# 4  4
# 9  6
# 16 8
class Solution(object):
    def judgeSquareSum0(self, c):
        """
        :type c: int
        :rtype: bool
        """
        square_list = list()
        for i in range(0, c / 2 + 2):
            square_list.append(i * i)
        for num in square_list:
            if c - num in square_list:
                return True
        return False

    def judgeSquareSum(self, c):
        for a in range(int(c ** 0.5) + 1):
            b2 = c - a ** 2
            if (int(b2 ** 0.5)) ** 2 == b2:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print s.judgeSquareSum(5)
    print s.judgeSquareSum(4)
    print s.judgeSquareSum(1)
    print s.judgeSquareSum(3)
    print s.judgeSquareSum(10000000)
