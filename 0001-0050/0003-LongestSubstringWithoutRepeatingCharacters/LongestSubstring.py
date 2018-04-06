# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/25
@version: 1.0.0.0
"""


class Solution(object):
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_length = 0
        pos_dict = dict()
        for i, v in enumerate(s):
            if v in pos_dict and start <= pos_dict[v]:
                start = pos_dict[v] + 1
            else:
                max_length = max(max_length, i - start + 1)
            pos_dict[v] = i
        return max_length

    def lengthOfLongestSubstring(self, s):
        ans, start, end = 0, 0, 0
        countDict = {}
        for c in s:
            end += 1
            countDict[c] = countDict.get(c, 0) + 1
            while countDict[c] > 1:
                countDict[s[start]] -= 1
                start += 1
            ans = max(ans, end - start)
        return ans


if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring("abcabcbb")
    print s.lengthOfLongestSubstring("bbbbb")
    print s.lengthOfLongestSubstring("pwwkew")
    print s.lengthOfLongestSubstring("tmmzuxt")
