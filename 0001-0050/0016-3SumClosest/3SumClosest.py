# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/4
@version: 1.0.0.0
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        min_num = target
        close_num = None
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            t_target = target - nums[i]
            while left < right:
                if left == 1 and right == len(nums) - 1:
                    min_num = abs(t_target - nums[left] - nums[right])
                    close_num = nums[i] + nums[left] + nums[right]
                elif abs(t_target - nums[left] - nums[right]) < min_num:
                    min_num = abs(t_target - nums[left] - nums[right])
                    close_num = nums[i] + nums[left] + nums[right]
                if nums[left] + nums[right] < t_target:
                    left += 1
                else:
                    right -= 1
                # print t_target, min_num, close_num, i, left, right
        return close_num


if __name__ == "__main__":
    s = Solution()
    print s.threeSumClosest([-1, 2, 1, -4], 1)
    print s.threeSumClosest([1, 1, 1, 1], 0)
    print s.threeSumClosest([1, 1, 1, 0], -100)
    print s.threeSumClosest([-3, 0, 1, 2], 1)  # 0
    print s.threeSumClosest([-1, 0, 1, 1, 55], 3)  # 2
