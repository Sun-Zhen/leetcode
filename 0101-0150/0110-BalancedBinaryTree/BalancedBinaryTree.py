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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = self.dfs(root)
        return res[2]

    def dfs(self, root):
        left = right = 1
        if root is None:
            print "a", [0, 0, True]
            return [0, 0, True]
        else:
            flag = True
            left_res = self.dfs(root.left)
            right_res = self.dfs(root.right)
            left += max(left_res[:2])
            right += max(right_res[:2])
            if not left_res[2] or not right_res[2] or abs(left - right) > 1:
                flag = False
            print "b", root.val, [left, right, flag]
            return [left, right, flag]


if __name__ == "__main__":
    a = [3, 9, 20, None, None, 15, 7]
    # head = TreeNode(3)
    # head.left = TreeNode(9)
    # head.right = TreeNode(20)
    # head.right.left = TreeNode(15)
    # head.right.right = TreeNode(7)
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.left.left = TreeNode(3)
    head.left.left.left = TreeNode(4)
    s = Solution()
    print s.isBalanced(head)
    # print s.isBalanced(None)
