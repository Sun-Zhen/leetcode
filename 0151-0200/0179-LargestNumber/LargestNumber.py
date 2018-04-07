# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, num):
        num = sorted([str(x) for x in num], cmp=self.compare)
        ans = ''.join(num).lstrip('0')
        return ans or '0'

    @staticmethod
    def compare(a, b):
        return [1, -1][a + b > b + a]


if __name__ == "__main__":
    s = Solution()
    s.compare("32", "21")
