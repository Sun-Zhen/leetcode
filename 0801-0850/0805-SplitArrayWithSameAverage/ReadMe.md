### 题目
* 给定的整数数组A，我们要将A数组中的每个元素移动到B数组或者C数组中。（B数组和C数组在开始的时候都为空）
* 返回true,当且仅当在我们的完成这样的移动后,可使得B数组的平均值和C数组的平均值相等，并且B数组和C数组都不为空。

```
示例:
输入: 
[1,2,3,4,5,6,7,8]
输出: true
解释: 我们可以将数组分割为[1,4,5,8]和[2,3,6,7], 他们的平均值都是4.5。
```
#### 注意:
* A 数组的长度范围为 [1, 30].
* A[i] 的数据范围为 [0, 10000].

#### 思路
* 排序
* 求整体平均值
* 这个问题可以抽象为:在一个有序数组里面找到n个元素的平均值等于指定值(指定值介于数组最大值与最小值范围之间)
* 拆分数组的长度=1
  拆分数组的长度=2
  拆分数组的长度=3
  ...
  拆分数组的长度=n-1
* 参考文档：https://leetcode.com/articles/split-array-with-same-average/