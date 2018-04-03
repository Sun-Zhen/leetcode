### 算法
* 动态规划

        # start = max_length = 0
        # used_char = dict()
        # 
        # for i in range(len(s)):
        #     if s[i] in used_char and start <= used_char[s[i]]:
        #         start = used_char[s[i]] + 1
        #     else:
        #         max_length = max(max_length, i - start + 1)
        #     used_char[s[i]] = i
        # 
        # return max_length