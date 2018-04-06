### 题目
* 有两个大小为 m 和 n 的排序数组 nums1 和 nums2 。
* 请找出两个排序数组的中位数并且总的运行时间复杂度为 O(log (m+n)) 。

示例 1:
```
nums1 = [1, 3]
nums2 = [2]

中位数是 2.0
```
示例 2:
```
nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5
```

#### 思路
* 思路1
  * 如果我们可以在两个数列中求出第K小的元素，便可以解决该问题
* 思路2
  * 中位数的定义是将一个集合分成2个等长的子集合，并且其中一个子集合总是大于另外一个子集合

### TODO
* https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn))-solution-with-explanation
