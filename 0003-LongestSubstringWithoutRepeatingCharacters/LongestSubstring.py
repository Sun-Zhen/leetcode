# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/25
@version: 1.0.0.0
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_length = 0
        pos_dict = dict()
        for i in range(len(s)):
            if s[i] in pos_dict and start <= pos_dict[s[i]]:
                start = pos_dict[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            pos_dict[s[i]] = i
        return max_length


if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring("tmmzuxt")
