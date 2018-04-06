# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/1
@version: 1.0.0.0
"""


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = None
        ans = cnt = 0
        for n in nums:
            if n > last:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
            last = n
        return max(ans, cnt)


if __name__ == "__main__":
    s = Solution()
    print s.findLengthOfLCIS([1, 3, 5, 4, 7])
    print s.findLengthOfLCIS([2, 2, 2, 2, 2])
