# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/2
@version: 1.0.0.0
"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        10，扣掉2个字符，判断后续字符
        01，扣掉3个字符，判断后续字符
        00，n-1，扣掉两个字符，判断后续字符
        """
        # if len(flowerbed) < n:
        #     return False
        # elif n == 0:
        #     return True
        # elif len(flowerbed) == 0:
        #     return False
        # elif len(flowerbed) == 1 and
        #     for i in range(len(flowerbed)):
        #         pass


if __name__ == "__main__":
    s = Solution()
    print s.canPlaceFlowers([1, 0, 0, 0, 1], 1)
    print s.canPlaceFlowers([1, 0, 0, 0, 1], 2)
    print s.canPlaceFlowers([0, 1, 0, 0, 0, 1], 2)
    print s.canPlaceFlowers([0, 0, 1, 0, 0, 0, 1], 2)
    print s.canPlaceFlowers([0, 0, 0, 1, 0, 0, 0, 1], 3)
    print s.canPlaceFlowers([0, 0, 0, 0, 1, 0, 0, 0, 1], 3)
