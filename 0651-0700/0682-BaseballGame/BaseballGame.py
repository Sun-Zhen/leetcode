# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/1
@version: 1.0.0.0
"""


class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = list()
        for i in ops:
            if i.isdigit() or (i[0] == "-" and i[1:].isdigit()):
                stack.append(int(i))
            elif i == "+":
                tmp = sum(stack[-2:])
                stack.append(tmp)
            elif i == "D":
                tmp = stack[-1] * 2
                stack.append(tmp)
            elif i == "C":
                del stack[-1]
        return sum(stack)


if __name__ == "__main__":
    s = Solution()
    print s.calPoints(["5", "2", "C", "D", "+"])
    print s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])
