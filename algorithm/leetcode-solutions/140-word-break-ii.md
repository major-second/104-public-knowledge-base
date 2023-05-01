- https://leetcode.cn/problems/word-break-ii
- [[dp]]
  - 注意顺序，我这里从后到前
  - [[off-by-one-errors#差一再差一]]
- 标答[[memo]]
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        length = len(s)
        ret_list = [[] for i in range(length)]
        for i in range(length-1, -1, -1):
            if s[i:] in wordDict:
                ret_list[i].append(s[i:])
            for j in range(i+1, length): # j_max = length-1
                if s[i:j] not in wordDict:
                    continue
                for sentence in ret_list[j]:
                    ret_list[i].append(f'{s[i:j]} {sentence}')
        return ret_list[0]
```