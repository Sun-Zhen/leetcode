# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = list()
        for _, v in enumerate(tokens):
            if v in ("+", "-", "*", "/"):
                t1 = stack[-2]
                t2 = stack[-1]
                del stack[-2]
                del stack[-1]
                if v == "+":
                    stack.append(t1 + t2)
                elif v == "-":
                    stack.append(t1 - t2)
                elif v == "*":
                    stack.append(t1 * t2)
                elif v == "/":
                    stack.append(int(float(t1) / t2))
            else:
                stack.append(int(v))
        return stack[0]


if __name__ == "__main__":
    s = Solution()
    # print s.evalRPN(["2", "1", "+", "3", "*"])
    # print s.evalRPN(["4", "13", "5", "/", "+"])
    # print s.evalRPN(["3", "-4", "+"])
    # print s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    # print s.evalRPN(["4", "-2", "/", "2", "-3", "-", "-"])
    print s.evalRPN(["4", "13", "5", "/", "+"])
