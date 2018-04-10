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


# 3
#  / \
# 9  20
#   /  \
#  15   7
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = list()
        queue = list()
        if root is not None:
            queue.append(root)
            while len(queue) != 0:
                next_row = list()
                temp_row = list()
                for i in range(len(queue)):
                    temp_row.append(queue[i].val)
                    if queue[i].left is not None:
                        next_row.append(queue[i].left)
                    if queue[i].right is not None:
                        next_row.append(queue[i].right)
                res.insert(0, temp_row)
                queue = next_row
        return res


if __name__ == "__main__":
    pass
