- https://leetcode.cn/problems/can-i-win/solutions/
- 参考
    - [[memo]]
    - [[6-adversarial-search#alpha-beta]]
    - [[for-else]]
- [[algorithm/special-case]]: 0情况，求和不足情况
- [[dp]]从后往前走，最坏[[complexity]]看起来一致
  - 但[[dp]]不会中途返回，没有任何[[enumerate#pruning]]，故会TLE
```python
from collections import defaultdict
class Solution:
    def search(self, memory, binary_code, start, desiredTotal):
        binary_code_tuple = tuple(binary_code)
        if memory[start][binary_code_tuple] < 0:
            for i, binary_digit in enumerate(binary_code):
                curr_number = i + 1
                if binary_digit == 0:
                    next_binary_code = binary_code[:i] + [1] + binary_code[i+1:]
                    next_binary_code_tuple = tuple(next_binary_code)
                    if start + curr_number >= desiredTotal or self.search(memory, next_binary_code, start + curr_number, desiredTotal) == False:
                        memory[start][binary_code_tuple] = True
                        break
            else:
                memory[start][binary_code_tuple] = False
        return memory[start][binary_code_tuple]
        
        

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal == 0:
            return True
        if desiredTotal > maxChoosableInteger * (maxChoosableInteger + 1) // 2:
            return False
        memory = [defaultdict(lambda:-1) for i in range(desiredTotal)]
        return self.search(memory, [0 for i in range(maxChoosableInteger)], 0, desiredTotal)
```