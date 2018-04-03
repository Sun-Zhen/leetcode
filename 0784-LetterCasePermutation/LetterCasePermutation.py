# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/29
@version: 1.0.0.0
"""


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = list()

        def dfs(S, pos, str):
            if pos == len(S):
                ans.append(str)
                return
            else:
                if S[pos].isalpha():
                    letter = S[pos]
                    dfs(S, pos + 1, str + letter.upper())
                    dfs(S, pos + 1, str + letter.lower())
                else:
                    dfs(S, pos + 1, str + S[pos])

        dfs(S, 0, '')
        return ans


if __name__ == "__main__":
    s = Solution()
    print s.letterCasePermutation("a1b2")
    print s.letterCasePermutation("3z4")
    print s.letterCasePermutation("12345")
