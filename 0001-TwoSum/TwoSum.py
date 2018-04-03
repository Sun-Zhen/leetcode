# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/3/25
@version: 1.0.0.0
"""


class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        final_list = list()
        flag = False
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    final_list.append(i)
                    final_list.append(j)
                    flag = True
                    break
            if flag:
                break
        return final_list

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp_dict = dict()
        for k, v in enumerate(nums):
            if target - v in tmp_dict:
                return [tmp_dict[target - v], k]
            else:
                tmp_dict[v] = k


if __name__ == "__main__":
    s = Solution()
    target_list = [3, 2, 3, 4]
    print s.twoSum(target_list, 7)
