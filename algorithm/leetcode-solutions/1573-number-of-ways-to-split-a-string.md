- 其实主要的坑是[[algorithm/special-case]]
  - 全0
  - 1数量不能被3整除
```python
class Solution:
    def numWays(self, s: str) -> int:
        MAGIC = 1000000007

        my_list = list(map(int, s))
        num_1 = sum(my_list)
        length = len(s)
        if num_1 == 0:
            return (length - 2) * (length - 1) // 2 % MAGIC
        elif num_1 % 3 != 0:
            return 0

        num_1_per_part = num_1 // 3

        curr_total = 0
        start = 0
        for i in range(length):
            curr_total += s[i] == '1'
            if curr_total == num_1_per_part:
                start = i
                break

        curr_total = 0
        end = 0
        for i in range(length-1, -1, -1):
            curr_total += s[i] == '1'
            if curr_total == num_1_per_part:
                end = i
                break

        relevant_part = s[start+1:end]
        left_choices = relevant_part.find('1') + 1
        right_choices = end - start - 1 - relevant_part.rfind('1')
        return left_choices % MAGIC * right_choices % MAGIC
```