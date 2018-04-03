# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/2
@version: 1.0.0.0
"""


#  1 <= k <= n <= 30,000。
#  所给数据范围 [-10,000，10,000]。

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        temp_max = None
        last_sum = None
        for i in range(len(nums) - k + 1):
            if i == 0:
                cur_sum = last_sum = sum(nums[:k])
            else:
                cur_sum = last_sum - nums[i - 1] + nums[i + k - 1]
                last_sum = cur_sum
            temp_max = max(float(cur_sum) / k, temp_max)
        return temp_max


if __name__ == "__main__":
    s = Solution()
    # print s.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
    # print s.findMaxAverage([-1], 1)
    print s.findMaxAverage([4, 2, 1, 3, 3], 2)
