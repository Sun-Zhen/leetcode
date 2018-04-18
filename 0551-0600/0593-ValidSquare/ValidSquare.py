# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/18
@version: 1.0.0.0
"""


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        任意一点与剩余三个点的距离为关系
        1.两个相等
        2.另外一个为剩下两个平方的和
        """
        line_list = list()
        line_list.append((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))
        line_list.append((p1[0] - p3[0]) * (p1[0] - p3[0]) + (p1[1] - p3[1]) * (p1[1] - p3[1]))
        line_list.append((p1[0] - p4[0]) * (p1[0] - p4[0]) + (p1[1] - p4[1]) * (p1[1] - p4[1]))
        line_list.append((p2[0] - p3[0]) * (p2[0] - p3[0]) + (p2[1] - p3[1]) * (p2[1] - p3[1]))
        line_list.append((p2[0] - p4[0]) * (p2[0] - p4[0]) + (p2[1] - p4[1]) * (p2[1] - p4[1]))
        line_list.append((p3[0] - p4[0]) * (p3[0] - p4[0]) + (p3[1] - p4[1]) * (p3[1] - p4[1]))
        line_dict = dict()
        for line in line_list:
            line_dict[line] = line_dict.get(line, 0) + 1
        key_list = line_dict.keys()
        if len(key_list) == 2 \
                and ((key_list[0] == 2 * key_list[1] and line_dict[key_list[0]] == 2)
                     or (key_list[1] == 2 * key_list[0] and line_dict[key_list[1]] == 2)):
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print s.validSquare([0, 0], [1, 1], [1, 0], [0, 1])  # True
    print s.validSquare([0, 0], [0, 0], [0, 0], [0, 0])
    print s.validSquare([1, 1], [0, 1], [1, 2], [0, 0])
    print s.validSquare([1, 0], [0, 1], [-1, 0], [0, -1])
