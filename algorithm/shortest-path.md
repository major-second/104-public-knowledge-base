- https://oiwiki.org/graph/shortest-path/
- dijkstra
  - 贪心[[greedy]]地每次找到离单源最近
  - 用[[adapter]]优先队列或二叉堆维护其它点到出发点的距离
    - 不是“到前沿的距离”！！
    - 对比[[minimum-spanning-tree]]中的prim
  - 如果用优先队列，由于不能删除之前不要的点，故更慢
  - 证明：[[induction]]，每一步都保证最优
    - 你填进一个点时，如果经由其它点到达，只会更差
    - 这里用到了无负权
    - 一条边对比了许多条边，所以不能整张图加某个数。对比[[minimum-spanning-tree]]中的prim算法
- floyd算法
  - 三重循环，每次“放松”一个可能中转点
  - 是一种[[dp]]算法，每次对$O(n^2)$个子问题都进行优中选优
  - 逻辑上两重循环，实现上三重循环
  - 实际操作中可以状态压缩
```python
# 初始时f是权（有限或正无穷）
for k in range(1, n + 1):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            f[x][y] = min(f[x][y], f[x][k] + f[k][y])
```
- bell算法：单源，在给出边列表时很适合。每次“放松”可能经过的边数
- floyd和bell的放松可以联系[[3-search]]中3.6节找启发式函数的“放松”