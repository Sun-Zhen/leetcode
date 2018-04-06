# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/31
@version: 1.0.0.0
"""


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(set(list(B)) - set(list(A))) > 0:
            return -1
        else:
            # 保证了字母集合一样
            times = 1
            gap = A
            while times >= 1:
                # print times, A, B
                if len(A) > 10000:
                    return -1
                elif len(A) < len(B):
                    times += 1
                    A += gap
                    continue
                else:
                    if B in A:
                        break
                    else:
                        A += gap
                times += 1
            return times


if __name__ == "__main__":
    s = Solution()
    # print s.repeatedStringMatch("abcd", "cdabcdab")
    print s.repeatedStringMatch("bb", "bbbbbbb")
