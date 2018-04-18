# -*- coding:utf-8 -*-
"""
@author: Alden
@email: sunzhenhy@gmail.com
@date: 2018/4/18
@version: 1.0.0.0
"""


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_dict = dict()
        for i, v in enumerate(list1):
            index_dict[v] = i
        min_index_sum = None
        res = list()
        for i, v in enumerate(list2):
            if v in index_dict:
                if min_index_sum is None:
                    min_index_sum = i + index_dict[v]
                    res.append(v)
                elif index_dict[v] + i < min_index_sum:
                    min_index_sum = index_dict[v] + i
                    res = [v]
                elif index_dict[v] + i == min_index_sum:
                    res.append(v)
        return res


if __name__ == "__main__":
    s = Solution()
    print s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                           ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse",
                            "Shogun"])
    print s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                           ["KFC", "Shogun", "Burger King"])
