### 题目
* 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 长度最长为1000。

示例:
```
输入: "babad"
输出: "bab"
注意: "aba"也是有效答案
```

示例:
```
输入: "cbbd"
输出: "bb"
```

#### 博文资料
* https://segmentfault.com/a/1190000008939789
* https://www.cnblogs.com/daoluanxiaozi/p/longest-palindromic-substring.html
* https://leetcode.com/problems/longest-palindromic-substring/solution/

#### 思路(奇回文串，偶回文串)
* 暴力遍历所有子串
  * 时间复杂度O(n<sup>3</sup>)
* 遍历所有可能存在的中心点
  * 遍历n个字符加上n+1个缝隙
  * 每个位置平均大约要进行n/4次比较
  * 时间复杂度为O(n<sup>2</sup>)
* 动态规划(DP)
  * 
* Manacher算法