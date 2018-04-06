# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/28
@version: 1.0.0.0
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = False if x >= 0 else True
        str_x = str(abs(x))
        str_res = ""
        for tmp in range(len(str_x)):
            str_res += str_x[len(str_x) - 1 - tmp]
        int_res = int(str_res)

        if is_negative and -1 * int_res > -1 * pow(2, 32):
            return -1 * int_res
        elif not is_negative and int_res < pow(2, 32) - 1:
            return int_res
        else:
            return 0


if __name__ == "__main__":
    s = Solution()
    print s.reverse(123)
    print s.reverse(-123)
    print s.reverse(120)
    print s.reverse(1)
