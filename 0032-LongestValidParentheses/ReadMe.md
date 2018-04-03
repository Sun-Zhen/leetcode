### 题目
* 给一个只包含 '(' 和 ')' 的字符串，找出最长的有效（正确关闭）括号子串的长度。
* 对于 "(()"，最长有效括号子串为 "()" ，它的长度是 2。
* 另一个例子 ")()())"，最长有效括号子串为 "()()"，它的长度是 4。

#### 思路
* 思路一(DP) 垃圾
  * 分解问题
    * 设F<sub>k</sub>为字符串中以第K项为结尾的子字符串的最长有效括号子串的长度
    * 求F<sub>1</sub> ... F<sub>N</sub>的最大值
    * F<sub>1</sub> = 0
    ```python
        stack = list()
        count_list = [[0, -1] for _ in range(len(s))]
        stack.append(s[0]) if len(s) > 0 else None
        for i in range(1, len(s)):
            if s[i] == "(":
                stack.append(s[i])
                if count_list[i - 1][1] > -1:
                    count_list[i][1] = count_list[i - 1][1]
                count_list[i][0] = count_list[i - 1][0]
            elif len(stack) - 1 >= 0 and stack[len(stack) - 1] == "(":
                # ()的情况
                if count_list[i - 1][1] > -1:
                    count_list[i][1] = count_list[i - 1][1] + 2
                else:
                    count_list[i][1] = 2
                count_list[i][0] = max([count_list[i - 1][0], count_list[i][1]])
                del (stack[len(stack) - 1])
            else:
                # ) 或者 )) 的情况
                count_list[i][1] = -1
                count_list[i][0] = count_list[i - 1][0]
        print count_list
        final_max = 0
        for i in count_list:
            final_max = max([final_max, i[0]])
        return final_max
    ```