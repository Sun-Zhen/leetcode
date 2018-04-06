# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/31
@version: 1.0.0.0
"""


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return True
        elif len(bits) == 2:
            if bits[0] == 1:
                return False
            else:
                return True
        else:
            if bits[0] == 0:
                return self.isOneBitCharacter(bits[1:])
            else:
                return self.isOneBitCharacter(bits[2:])


if __name__ == "__main__":
    s = Solution()
    print s.isOneBitCharacter([1, 0, 0])
    print s.isOneBitCharacter([1, 1, 1, 0])
    print s.isOneBitCharacter([0, 1, 0])
