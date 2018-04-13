# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/13
@version: 1.0.0.0
"""
import collections


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        s_dict = dict()
        for t in S:
            s_dict[t] = s_dict.get(t, 0) + 1
        temp_s = list()
        for k, v in sorted(s_dict.items(), key=lambda x: x[1], reverse=True):
            temp_s.extend([k] * v)
        all_length = len(S)
        if (all_length % 2 == 0 and s_dict[temp_s[0]] > all_length / 2) or \
                (all_length % 2 == 1 and s_dict[temp_s[0]] > all_length / 2 + 1):
            return ""
        else:
            mid = all_length / 2 if all_length % 2 == 0 else all_length / 2 + 1
            res = ""
            print mid, temp_s
            for i in range(mid):
                if mid + i < all_length:
                    res += (temp_s[i] + temp_s[mid + i])
                else:
                    res += temp_s[i]
            return res


if __name__ == "__main__":
    """
    n n-1 = 2n-1  n-1
    """
    s = Solution()
    # print s.reorganizeString("aab")  # "aba"
    # print s.reorganizeString("aaab")  # ""
    print s.reorganizeString("vvvlo")
