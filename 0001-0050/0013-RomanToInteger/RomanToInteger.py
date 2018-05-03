# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/28
@version: 1.0.0.0
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i, v in enumerate(s):
            if i + 1 < len(s) and roman_dict[s[i + 1]] > roman_dict[v]:
                res -= roman_dict[v]
            else:
                res += roman_dict[v]
        return res


if __name__ == "__main__":
    s = Solution()
    print s.romanToInt("III")
    print s.romanToInt("IV")
    print s.romanToInt("IX")
    print s.romanToInt("LVIII")
    print s.romanToInt("MCMXCIV")
