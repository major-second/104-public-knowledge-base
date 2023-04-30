- https://leetcode.cn/problems/stream-of-characters
```python
from collections import defaultdict

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = defaultdict(dict)
        for w in words:
            curr_node = self.trie
            for l in w:
                if l not in curr_node['children']:
                    curr_node['children'][l] = defaultdict(dict)
                curr_node = curr_node['children'][l]
            curr_node['is_a_word'] = True
        
        self.open_queries = {}

    def query(self, letter: str) -> bool:
        ret = False
        self.open_queries[''] = self.trie
        for k, v in list(self.open_queries.items()):
            del self.open_queries[k]
            if letter not in v['children']:
                continue
            v = v['children'][letter]
            self.open_queries[k + letter] = v
            ret |= bool(v['is_a_word'])
        return ret
```