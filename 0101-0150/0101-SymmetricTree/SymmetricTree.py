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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is not None:
            return self.is_equal(root.left, root.right)
        else:
            return True

    def is_equal(self, left, right):
        """
        :param left: 
        :param right: 
        :return: 
        """
        if left is not None and right is not None:
            return left.val == right.val and \
                   self.is_equal(left.left, right.right) and \
                   self.is_equal(left.right, right.left)
        elif left is None and left == right:
            return True
        else:
            return False


if __name__ == "__main__":
    pass
