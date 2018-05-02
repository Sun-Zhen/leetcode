# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/4
@version: 1.0.0.0
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        divisor = 1000
        res = ""
        roman_dict = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        while divisor != 0:
            t, r = num / divisor, num % divisor
            # print num, divisor, t, r
            if t != 0:
                if t == 4:
                    k1, k2 = divisor * 5, divisor
                    res += (roman_dict[k2] + roman_dict[k1])
                elif t == 9:
                    k1, k2 = divisor * 10, divisor
                    res += (roman_dict[k2] + roman_dict[k1])
                elif t >= 5:
                    k1, k2 = divisor * 5, divisor
                    res += (roman_dict[k1] + roman_dict[k2] * (t - 5))
                else:
                    k1 = divisor
                    res += (roman_dict[k1] * t)
            divisor /= 10
            num = r
        return res


if __name__ == "__main__":
    s = Solution()
    print s.intToRoman(3)  # "III"
    print s.intToRoman(4)  # "IV"
    print s.intToRoman(9)  # "IX"
    print s.intToRoman(58)  # "LVIII"
    print s.intToRoman(1994)  # "MCMXCIV"
