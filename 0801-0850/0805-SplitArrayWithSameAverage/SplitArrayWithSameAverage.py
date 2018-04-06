# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/28
@version: 1.0.0.0
"""


class Solution(object):
    def splitArraySameAverage(self, A):
        """
        抽象问题为从一个数组里面找到N个元素的平均值为target_value
        :type A: List[int]
        :rtype: bool
        """
        temp_list = sorted(A)  # O(n*n)
        avg_value = float(sum(temp_list)) / len(temp_list)  # 求平均值
        length = 1
        while length <= len(temp_list) - 1:
            pass
        return True


if __name__ == "__main__":
    s = Solution()
    s.splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8])
