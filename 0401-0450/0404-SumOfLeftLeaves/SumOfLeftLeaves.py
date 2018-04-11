# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/11
@version: 1.0.0.0
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = list()
        queue.append(root)
        res = list()
        while len(queue) != 0:
            next_queue = list()
            for temp_node in queue:
                if temp_node.left is not None:
                    next_queue.append(temp_node.left)
                    if temp_node.left.left is None and temp_node.left.right is None:
                        res.append(temp_node.left.val)
                if temp_node.right is not None:
                    next_queue.append(temp_node.right)
            queue = next_queue
        return sum(res)


if __name__ == "__main__":
    pass
