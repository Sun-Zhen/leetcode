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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.dfs(root, 0, sum)

    def dfs(self, root, sum_val, target):
        if root is not None:
            temp_sum = sum_val + root.val
            left_res = right_res = False
            if root.left is not None:
                left_res = self.dfs(root.left, temp_sum, target)
            if root.right is not None:
                right_res = self.dfs(root.right, temp_sum, target)
            if root.right is None and root.left is None and sum_val + root.val == target:
                return True
            elif root.right is None and root.left is None and sum_val + root.val != target:
                return False
            return left_res or right_res
        else:
            return False


if __name__ == "__main__":
    pass
