# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.split(nums, 0, len(nums) - 1)

    def split(self, nums, left, right):
        """
        
        :param nums: 
        :param left: 
        :param right: 
        :return: 
        """
        if left > right:
            return None
        mid = (left + right) / 2
        head = TreeNode(nums[mid])
        head.left = self.split(nums, left, mid - 1)
        head.right = self.split(nums, mid + 1, right)
        return head


if __name__ == "__main__":
    s = Solution()
    res = s.sortedArrayToBST([-10, -3, 0, 5, 9])
