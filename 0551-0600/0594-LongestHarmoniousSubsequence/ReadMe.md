### 题目
* 和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
* 现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

**示例 1:**
```
输入: [1,3,2,2,5,2,3,7]   1,3,2,5,7
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].
说明: 输入的数组长度最大不超过20,000.
```

### 自己想的方法1
```python
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_max_dict = dict()  # 比当前key大1
        len_min_dict = dict()
        check_list = list()
        if nums is None or len(nums) == 0:
            return 0
        for i, v in enumerate(nums):
            if v in len_max_dict:
                len_max_dict[v] += 1
            else:
                len_max_dict[v] = 1
            if v + 1 in len_max_dict:
                len_max_dict[v + 1] += 1
                check_list.extend([v, v + 1])

            if v in len_min_dict:
                len_min_dict[v] += 1
            else:
                len_min_dict[v] = 1
            if v - 1 in len_min_dict:
                len_min_dict[v - 1] += 1
                check_list.extend([v, v - 1])
        temp_max = 0
        for _, v in enumerate(check_list):
            temp_max = max(temp_max, len_max_dict[v])
            temp_max = max(temp_max, len_min_dict[v])
        return temp_max
```

### 参考别人的想法
> 找出来相差为1的两个数的总共出现个数就是一个和谐子序列的长度
> 参考博客为:http://www.cnblogs.com/grandyang/p/6896799.html
```python
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_dict = dict()
        for v in nums:
            temp_dict[v] = temp_dict.get(v, 0) + 1
        temp_max = 0
        for k, v in temp_dict.items():
            if k - 1 in temp_dict:
                temp_max = max(temp_max, v + temp_dict[k - 1])
            if k + 1 in temp_dict:
                temp_max = max(temp_max, v + temp_dict[k + 1])
        return temp_max

```