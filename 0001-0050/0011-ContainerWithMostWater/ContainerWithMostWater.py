# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/4
@version: 1.0.0.0
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        t_left, t_right = 0, len(height) - 1
        while t_left < t_right:
            max_area = max(max_area, min(height[t_right], height[t_left]) * (t_right - t_left))
            if height[t_left] < height[t_right]:
                t_left += 1
            else:
                t_right -= 1
            print t_left, t_right
        return max_area


if __name__ == "__main__":
    s = Solution()
    print s.maxArea([1, 2, 3, 4])
    print s.maxArea([1, 1])
