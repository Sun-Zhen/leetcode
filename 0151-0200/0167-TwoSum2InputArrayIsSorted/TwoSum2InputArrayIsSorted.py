# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        mid = (right - left) / 2
        print numbers[left], numbers[mid]
        while numbers[left] + numbers[mid] != target:
            if numbers[left] + numbers[mid] < target:
                left = mid
            else:
                right = mid
            mid = (right - left) / 2
        return [left + 1, mid + 1]


if __name__ == "__main__":
    s = Solution()
    # s.twoSum([2, 7, 11, 15], 9)
    # s.twoSum([1, 2, 7, 11, 15], 8)
    print s.twoSum([2, 3, 4], 6)
