# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/16
@version: 1.0.0.0
"""


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        word_dict = dict()
        punctuations = ["!", "?", "'", ",", ";", "."]
        temp_word = ""
        for v in paragraph:
            if v in punctuations:
                continue
            if v == " ":
                if temp_word != "" and temp_word not in banned:
                    word_dict[temp_word] = word_dict.get(temp_word, 0) + 1
                temp_word = ""
            else:
                temp_word += v.lower()
        if temp_word != "" and temp_word not in banned:
            word_dict[temp_word] = word_dict.get(temp_word, 0) + 1
        return sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[0][0]


if __name__ == "__main__":
    s = Solution()
    # print s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    print s.mostCommonWord("a.", [])
