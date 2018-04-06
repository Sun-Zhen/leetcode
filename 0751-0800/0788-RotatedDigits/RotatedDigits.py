# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/29
@version: 1.0.0.0
"""


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        white_list = ["2", "5", "6", "9"]
        other_list = ["3", "4", "7"]
        for tmp in range(N + 1):
            flag = False
            for i in str(tmp):
                if i in white_list:
                    flag = True
                if i in other_list:
                    flag = False
                    break
            res = res + 1 if flag else res
        return res


if __name__ == "__main__":
    s = Solution()
    print s.rotatedDigits(857)
