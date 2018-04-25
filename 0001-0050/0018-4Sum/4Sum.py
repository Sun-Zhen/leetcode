# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/5
@version: 1.0.0.0
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        sum_dict = dict()
        res = list()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum_dict.setdefault(nums[i] + nums[j], list()).append([i, j])
        # for k, v in sum_dict.items():
        #     print k, v
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if target - nums[i] - nums[j] in sum_dict:
                    tmp_array = sum_dict[target - nums[i] - nums[j]]
                    first_flag = True
                    for t_index in range(len(tmp_array)):
                        if (first_flag and tmp_array[t_index][0] > j) or (tmp_array[t_index][0] > j and nums[tmp_array[t_index][0]] != res[-1][2]):
                            t = [nums[i], nums[j]]
                            t.extend([nums[tmp_array[t_index][0]], nums[tmp_array[t_index][1]]])
                            res.append(t)
                            first_flag = False
        return res


if __name__ == "__main__":
    s = Solution()
    print s.fourSum([1, 0, -1, 0, -2, 2], 0)
    print s.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)
    print s.fourSum([-2, -1, 0, 0, 1, 2], 0)
