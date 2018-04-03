
实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 匹配任何单个字符。
'*' 匹配任何数量的字符 (包括0个)。

匹配应覆盖 整个 输入字符串（而不是部分）。

这个函数原型为：
bool isMatch(const char *s, const char *p)

示例：
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false