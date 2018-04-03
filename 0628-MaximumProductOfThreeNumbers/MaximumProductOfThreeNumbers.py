# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/2
@version: 1.0.0.0
"""


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        绝对值最大前三，原始值
        绝对值最小前三，原始值
        
        或者
        
        正数 两个最小负数一个最大正数，三个最大正数
        负数 两个最小正数一个最大负数，三个最大负数
        """
        ans = pa = pb = pc = None
        na = nb = 0x7FFFFFFF
        for n in nums:
            if n > pa:
                pa, pb, pc = n, pa, pb
            elif n > pb:
                pb, pc = n, pb
            elif n > pc:
                pc = n
            if n < na:
                na, nb = n, na
            elif n < nb:
                nb = n
        return max(ans, pa * na * nb, pa * pb * pc)


if __name__ == "__main__":
    s = Solution()
    # print s.maximumProduct([1, 2, 3])
    # print s.maximumProduct([1, 2, 3, 4])
    # print s.maximumProduct([1000, 1000, 1000])
    print s.maximumProduct([2, -2, -1, -3])
