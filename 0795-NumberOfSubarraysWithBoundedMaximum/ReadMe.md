### 题目
* 给定一个元素都是正整数的数组A，正整数L以及R(L<=R)。
* 求连续、非空且数值最大的元素满足大于等于L小于等于R的子数组个数。

```
例如 :
输入: 
A = [2, 1, 4, 3]
L = 2
R = 3
输出: 3
解释: 满足条件的子数组: [2], [2, 1], [3].
```

#### 注意:
* L, R  和 A[i] 都是整数，范围在 [0, 10^9]。
* 数组 A 的长度范围在[1, 50000]。

#### 思路
* 思路一:(执行超时，遍历任意连续子串)
```python
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        O(n*n)
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        gap = 1
        sum_count = 0
        while gap < len(A):
            index = 0
            while index < len(A) - gap + 1:
                if L <= max(A[index:index + gap]) <= R:
                    sum_count += 1
                index += 1
            gap += 1
        return sum_count
```
* 思路二:()
```python

```