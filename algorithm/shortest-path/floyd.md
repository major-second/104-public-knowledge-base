- 三重循环，每次“放松”一个可能中转点
- 是一种[[dp]]算法，每次对$O(n^2)$个子问题都进行[[dp#优中选优]]
- **逻辑上两重循环，实现上三重循环**
- 实际操作中可以[[dp#状态压缩]]（容易论证压缩不影响）
```python
from collections import defaultdict
f = defaultdict(lambda:defaultdict(lambda:float('inf')))
f[0][1] = f[1][2] = f[2][3] = 2
f[1][3] = f[0][3] = 5
n = 4
for k in range(n):
    for x in range(n):
        for y in range(n):
            f[x][y] = min(f[x][y], f[x][k] + f[k][y])
    
    for x in range(n):
        for y in range(n):
            print(k, x, y, f[x][y])
```