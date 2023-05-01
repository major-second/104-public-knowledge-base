- https://leetcode.cn/problems/palindrome-pairs
- 一个错解
  - 使用[[bisect]]
  - 问题：`sa, sabcc, sad`对上`as`，则可行的解范围不一定连续。我想当然了
```python
from bisect import bisect

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        reversed_words = [w[::-1] for w in words]
        num_words = len(words)
        words2index = sorted([(w, i) for (i, w) in enumerate(words)])
        reversed_words2index = sorted([(w, i) for (i, w) in enumerate(reversed_words)])
        ret = []

        def check(i, j):
            a = words[i]
            b = reversed_words[j]
            len_a = len(a)
            len_b = len(b)
            if len_a < len_b:
                a, b = b, a
                len_a, len_b = len_b, len_a
                # len_a >= len_b
            if a[:len_b] != b:
                return -1
            left = len_b
            right = len_a - 1
            while left < right:
                if a[left] != a[right]:
                    return 0
                left += 1
                right -= 1
            return 1
        
        for w, i in words2index:
            pivot = bisect(reversed_words2index, (w, i))

            curr_j = pivot
            while 0 <= curr_j < num_words:
                j = reversed_words2index[curr_j][1]
                curr_j += 1
                if i == j:
                    continue

                check_res = check(i, j)
                if check_res == 1:
                    ret.append((i, j))
                elif check_res == -1:
                    break

            curr_j = pivot - 1
            while 0 <= curr_j < num_words:
                j = reversed_words2index[curr_j][1]
                curr_j -= 1
                if i == j:
                    continue
                
                check_res = check(i, j)
                if check_res == 1:
                    ret.append((i, j))
                elif check_res == -1:
                    break
        return ret
```
- 一个正解
    - 有[[symmetry#翻转]]思想
    - ```python
        class Solution:
            def palindromePairs(self, words: List[str]) -> List[List[int]]:
                reversed_words = [w[::-1] for w in words]
                words2index = {w: i for (i, w) in enumerate(words)}
                reversed_words2index = {w: i for (i, w) in enumerate(reversed_words)}
                ret = set()

                for i, w in enumerate(words):
                    curr_length = len(w)
                    for k in range(curr_length + 1):
                        prefix = w[:k]
                        suffix = w[k:]
                        if prefix in reversed_words2index and suffix == suffix[::-1]:
                            j = reversed_words2index[prefix]
                            if i != j:
                                ret.add((i, j))

                for i, w in enumerate(reversed_words):
                    curr_length = len(w)
                    for k in range(curr_length + 1):
                        prefix = w[:k]
                        suffix = w[k:]
                        if prefix in words2index and suffix == suffix[::-1]:
                            j = words2index[prefix]
                            if i != j:
                                ret.add((j, i))
                return list(ret)
      ```
- 当然还可使用[[trie]]（难度高）