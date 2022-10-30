- https://leetcode.com/problems/repeated-string-match/
# python调包赖皮法
```python
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        b_first_index = b.find(a)
        if b_first_index == -1:
            if b in a:
                return 1
            if b in a * 2:
                return 2
            return -1
        
        b_l, b_r = b[:b_first_index], b[b_first_index:]
        l_l, l_r, l_a = len(b_l), len(b_r), len(a)
        
        if l_l and a[-l_l:] != b_l:
            return -1
        left_additional = bool(l_l)
        
        potential_right_times = l_r // l_a + bool(l_r % l_a)
        a_repeated = a * potential_right_times
        return -1 if a_repeated[:l_r] != b_r else left_additional + potential_right_times
```
- 一个要点：`l_l==0`时，注意`-0`还是`0`，`if l_l and a[-l_l:] != b_l:`会有意料之外结果
- 一个思维盲区：`ba`在`abab`中，所以如果一来找不到，则结果可能是`1, 2, -1`，不能漏掉`2`的可能
# python最简洁赖皮法
```python
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(b) // len(a)
        a_repeated = a * n
        for i in range(3):
            if b in a_repeated: return n + i
            a_repeated += a
        return -1
```