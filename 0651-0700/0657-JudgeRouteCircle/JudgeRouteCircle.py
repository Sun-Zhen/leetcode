# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/1
@version: 1.0.0.0
"""


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dict1 = {"U": 1, "D": -1}
        dict2 = {"L": 1, "R": -1}
        res1 = 0
        res2 = 0
        for i in moves:
            if i in dict1.keys():
                res1 += dict1[i]
            else:
                res2 += dict2[i]
        if res1 == res2 and res1 == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print s.judgeCircle("UD")
    print s.judgeCircle("LL")
