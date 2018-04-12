# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/28
@version: 1.0.0.0
"""


class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        if not A: return 0
        dp = [0 for _ in range(len(A))]
        dp[0] = 1 if L <= A[0] <= R else 0

        for i in range(1, len(A)):
            if A[i] > R:
                continue
            if A[i] < L:
                dp[i] = dp[i - 1]
            else:
                j = i - 1
                # 处理遗漏的情况
                while j >= 0 and A[j] < L:
                    j -= 1
                dp[i] = dp[i - 1] + i - j
        return dp


if __name__ == "__main__":
    s = Solution()
    print (s.numSubarrayBoundedMax([1, 1, 3, 1, 3], 2, 4))
