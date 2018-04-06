### 题目
* 实现支持 '.' 和 '*' 的正则表达式匹配。
```
'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。

匹配应该覆盖整个输入字符串（不是部分字符串）。

函数:
bool isMatch(const char *s, const char *p)

例子:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
```
