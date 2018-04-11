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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        else:
            left = self.binaryTreePaths(root.left)
            right = self.binaryTreePaths(root.right)
            temp_val = str(root.val)
            res = list()
            res.extend([] if len(left) == 0 else left)
            res.extend([] if len(right) == 0 else right)
            final_res = list()
            if len(res) == 0:
                final_res.append(temp_val)
            else:
                for temp in res:
                    temp = temp_val + "->" + temp
                    final_res.append(temp)
            return final_res

    # def dfs(self, root):
    #     """
    #     :param root: TreeNode
    #     :return:
    #     """
    #     if root is None:
    #         return [""]
    #     else:
    #         left = self.dfs(root.left)
    #         right = self.dfs(root.right)
    #         temp_val = str(root.val)
    #         res = list()
    #         res.extend([] if len(left) == 1 and left[0] == "" else left)
    #         res.extend([] if len(right) == 1 and right[0] == "" else right)
    #         final_res = list()
    #         if len(res) == 0:
    #             final_res.append(temp_val)
    #         else:
    #             for temp in res:
    #                 temp = temp_val + "->" + temp
    #                 final_res.append(temp)
    #         return final_res


if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.right = TreeNode(5)
    s = Solution()
    print s.binaryTreePaths(head)
