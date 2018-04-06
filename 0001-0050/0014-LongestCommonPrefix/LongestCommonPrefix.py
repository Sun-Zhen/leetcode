# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/28
@version: 1.0.0.0
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        final_res = ""
        if len(strs) == 0:
            return final_res
        len_list = list()
        for i in range(len(strs)):
            len_list.append(len(strs[i]))
        for i in range(1, min(len_list) + 1):
            for j in range(len(strs) - 1):
                if strs[j][:i] != strs[j + 1][:i]:
                    return final_res
            final_res = strs[0][:i]
        return final_res


if __name__ == "__main__":
    s = Solution()
    print (s.longestCommonPrefix(["a"]))
