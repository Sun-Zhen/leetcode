# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        t_dict = dict()
        a = "a"
        for i in range(2, 10):
            if i not in [7, 9]:
                t_dict[str(i)] = [chr(ord(a)), chr(ord(a) + 1), chr(ord(a) + 2)]
                a = chr(ord(a) + 3)
            else:
                t_dict[str(i)] = [chr(ord(a)), chr(ord(a) + 1), chr(ord(a) + 2), chr(ord(a) + 3)]
                a = chr(ord(a) + 4)
        res = list()

        def dfs(t_str, digits):
            if len(digits) == 0 and len(t_str) != 0:
                res.append(t_str)
            elif len(digits) > 0:
                for t in t_dict[digits[0]]:
                    dfs(t_str + t, digits[1:])

        dfs("", digits=digits)
        return res


if __name__ == "__main__":
    s = Solution()
    print s.letterCombinations("23")
    print s.letterCombinations("")
    print s.letterCombinations("7")
