# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/31
@version: 1.0.0.0
"""


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target < letters[0] or target >= letters[len(letters) - 1]:
            return letters[0]
        else:
            for i in letters:
                if i > target:
                    return i


if __name__ == "__main__":
    s = Solution()
    print s.nextGreatestLetter(["c", "f", "j"], "j")
