# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/30
@version: 1.0.0.0
"""


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        target_list = list()
        for tmp in J:
            target_list.append(tmp)
        for tmp in S:
            if tmp in target_list:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    s.numJewelsInStones("aA", "aAAbbbb")
    s.numJewelsInStones("z", "ZZ")
