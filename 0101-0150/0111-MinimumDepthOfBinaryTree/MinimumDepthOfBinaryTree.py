# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/6
@version: 1.0.0.0
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            res = 0
            queue = list()
            queue.append(root)
            while len(queue) != 0:
                temp_queue = list()
                for i in range(len(queue)):
                    if queue[i].left is None and queue[i].right is None:
                        return res + 1
                    if queue[i].left is not None:
                        temp_queue.append(queue[i].left)
                    if queue[i].right is not None:
                        temp_queue.append(queue[i].right)
                res += 1
                print res, len(queue)
                queue = temp_queue
            return res


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    s = Solution()
    print s.minDepth(head)
