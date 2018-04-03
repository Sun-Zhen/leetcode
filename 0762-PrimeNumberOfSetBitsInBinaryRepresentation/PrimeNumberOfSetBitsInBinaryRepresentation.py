# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/30
@version: 1.0.0.0
"""


# L, R will be integers L <= R in the range [1, 10^6].
# R - L will be at most 10000.

class Solution(object):
    def __init__(self):
        max_bit_len = len(bin(int(1e6))[2:])
        self.prime_nums = list()
        for i in range(2, max_bit_len + 1):
            flag = True
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
            self.prime_nums.append(i) if flag else None

    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        final_res = 0
        for target_value in range(L, R + 1):
            tmp_val = list(bin(target_value)[2:])
            tmp_list = list()
            [tmp_list.append("1") if i == "1" else None for i in tmp_val]
            if len(tmp_list) in self.prime_nums:
                final_res += 1
        return final_res


if __name__ == "__main__":
    s = Solution()
    print s.countPrimeSetBits(842, 888)
