# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/29
@version: 1.0.0.0
"""


# 示例 1:
# 输入: A = 'abcde', B = 'cdeab'
# 输出: true
# 示例 2:
# 输入: A = 'abcde', B = 'abced'
# 输出: false

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            return True
        else:
            for i in range(1, len(A)):
                if A[i:] + A[0:i] == B:
                    return True
            return False


if __name__ == "__main__":
    s = Solution()
    print s.rotateString('abcde', 'cdeab')
    print s.rotateString('abcde', 'abced')
