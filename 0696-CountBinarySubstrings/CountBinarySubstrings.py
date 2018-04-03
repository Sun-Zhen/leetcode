# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/31
@version: 1.0.0.0
"""


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        final_res = 0
        mid_list = list()
        mid_list.append(1 if s[0] == "1" else -1)
        for tmp in s[1:]:
            if tmp == "1":
                if mid_list[len(mid_list) - 1] > 0:
                    mid_list[len(mid_list) - 1] += 1
                else:
                    mid_list.append(1)
            else:
                if mid_list[len(mid_list) - 1] > 0:
                    mid_list.append(-1)
                else:
                    mid_list[len(mid_list) - 1] += -1
        if len(mid_list) == 1:
            return 0
        for i in range(len(mid_list) - 1):
            final_res += min([abs(mid_list[i]), abs(mid_list[i + 1])])
        return final_res


if __name__ == "__main__":
    s = Solution()
    print s.countBinarySubstrings("00110011")
    print s.countBinarySubstrings("10101")
