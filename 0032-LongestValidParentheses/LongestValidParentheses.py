# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/29
@version: 1.0.0.0
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = t_max = 0
        stack = list()
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    start = i + 1
                else:
                    del stack[len(stack) - 1]
                    if len(stack) == 0:
                        t_max = max(t_max, i - start + 1)
                    else:
                        t_max = max(t_max, i - stack[len(stack) - 1])
        return t_max


if __name__ == "__main__":
    s = Solution()
    print s.longestValidParentheses("()(()")
    print s.longestValidParentheses(")()())()()()")
    print s.longestValidParentheses("()(())")
    print s.longestValidParentheses("(()")
    print s.longestValidParentheses("(")
    print s.longestValidParentheses(")")
    print s.longestValidParentheses("()")
    print s.longestValidParentheses("")
