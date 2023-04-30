- https://leetcode.cn/problems/distinct-subsequences/
```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        total = 0
        len_s = len(s)
        len_t = len(t)

        prev_dp_col = [0] * len_t
        curr_dp_col = [0] * len_t
        for i in range(len_s):
            for j in range(len_t):
                curr_dp_col[j] = prev_dp_col[j]
                if s[i] == t[j]:
                    if j == 0:
                        curr_dp_col[j] += 1
                    else:
                        curr_dp_col[j] += prev_dp_col[j - 1]
            prev_dp_col, curr_dp_col = curr_dp_col, [0] * len_t
        return prev_dp_col[-1]
```
- [[dp#状态压缩]]
- [[dp#计数方案数]]