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
    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        res = self.dfs(root, p, q)
        return res[0]

    def lowestCommonAncestor(self, root, p, q):
        while (p.val - root.val) * (q.val - root.val) > 0:
            root = [root.left, root.right][p.val > root.val]
        return root

    def dfs(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :return: 
        """
        if root is None:
            return [None, False, False]
        else:
            left_res = right_res = None
            res = [None, False, False]
            if root.left is not None:
                left_res = self.dfs(root.left, p, q)
                if left_res[0] is not None and left_res[1] and left_res[2]:
                    return left_res
            if root.right is not None:
                right_res = self.dfs(root.right, p, q)
                if right_res[0] is not None and right_res[1] and right_res[2]:
                    return right_res
            if root.val == q.val or \
                    (left_res is not None and left_res[2]) or \
                    (right_res is not None and right_res[2]):
                res[2] = True
            if root.val == p.val or \
                    (left_res is not None and left_res[1]) or \
                    (right_res is not None and right_res[1]):
                res[1] = True
            if res[1] and res[2]:
                res[0] = root
            return res


if __name__ == "__main__":
    head = TreeNode(2)
    head.left = TreeNode(1)
    print head.val
    print head.left.val
    s = Solution()
    print s.lowestCommonAncestor(head, TreeNode(2), TreeNode(1)).val
