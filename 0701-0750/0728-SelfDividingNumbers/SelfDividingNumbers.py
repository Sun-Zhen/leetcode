# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/31
@version: 1.0.0.0
"""


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        final_res = list()
        for i in range(left, right + 1):
            tmp_value = str(i)
            if "0" not in list(tmp_value):
                flag = True
                for j in list(tmp_value):
                    if i % int(j) != 0:
                        flag = False
                        break
                if flag:
                    final_res.append(i)
        return final_res


if __name__ == "__main__":
    s = Solution()
    print s.selfDividingNumbers(1, 22)
