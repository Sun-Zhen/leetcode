### 题目
* 将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：（下面这样的形状）
```
P   A   H   N
A P L S I I G
Y   I   R
```
* 之后按逐行顺序依次排列："PAHNAPLSIIGYIR"

* 实现一个将字符串进行指定行数的转换的函数:
```
string convert(string text, int nRows);
```
convert("PAYPALISHIRING", 3) 应当返回 "PAHNAPLSIIGYIR" 。