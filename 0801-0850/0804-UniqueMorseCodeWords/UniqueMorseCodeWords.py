# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/29
@version: 1.0.0.0
"""


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        tmp_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-",
                    ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-",
                    ".--", "-..-", "-.--", "--.."]
        tmp_dict = dict()
        for i in range(len(tmp_list)):
            tmp_dict[chr(97 + i)] = tmp_list[i]
        words_list = list()
        for word in words:
            tmp_str = ""
            for l in word:
                tmp_str += tmp_dict[l]
            words_list.append(tmp_str)
        return len(set(words_list))


if __name__ == "__main__":
    s = Solution()
    s.uniqueMorseRepresentations()
