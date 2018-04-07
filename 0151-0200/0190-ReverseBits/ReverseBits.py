# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for _ in range(32):
            res <<= 1
            tmp = n & 1
            if tmp == 1:
                res |= 1
            n >>= 1
        return res


if __name__ == "__main__":
    s = Solution()
    print s.reverseBits(43261596)
