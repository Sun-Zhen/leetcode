# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/29
@version: 1.0.0.0
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = {"(": 0, "{": 1, "[": 2}
        right = {")": 0, "}": 1, "]": 2}
        stack = list()
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            else:
                if i in left:
                    stack.append(i)
                elif stack[len(stack) - 1] in left and left[stack[len(stack) - 1]] == right[i]:
                    del stack[len(stack) - 1]
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print s.isValid("()[]{}")
    print s.isValid("([)]")
