### 题目
* 给定一个字符串和一个字符串字典, 
* 寻找到字典里面最长的字符，该字符串可以通过删除给定字符串的某些字符来得到。
* 如果结果不止一个的话，返回长度最长且字典顺序最小的字符串。
* 如果没有的话，则返回空字符串。

**例子 1:**
```
输入:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

输出: 
"apple"
```

**例子 2:**
```
输入:
s = "abpcplea", d = ["a","b","c"]

输出: 
"a"
```

**注:**
* 输入的所有字符串只包含小写字母.
* 字典的大小不会超过 1,000.
* 输入的所有字符串长度不会超过 1,000.