# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/3
@version: 1.0.0.0
"""


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = 0
        is_positive = None
        for i, v in enumerate(str):
            if res == 0:
                if v == " " and is_positive is None:
                    continue
                elif v == "+" and is_positive is None:
                    is_positive = True
                elif v == "-" and is_positive is None:
                    is_positive = False
                elif v.isdigit():
                    res += int(v)
                else:
                    return 0
            else:
                if v.isdigit():
                    res = res * 10 + int(v)
                else:
                    break
        is_positive = True if is_positive is None else is_positive
        res = res if is_positive else res * -1
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        elif res < -1 * 2 ** 31:
            res = -1 * 2 ** 31
        return res


if __name__ == "__main__":
    s = Solution()
    print s.myAtoi("  01")
    print s.myAtoi("  -11")
    print s.myAtoi("   2147483648")
    print s.myAtoi("   a2147483648")
    print s.myAtoi("+-2")
    print s.myAtoi("   +0 123")
