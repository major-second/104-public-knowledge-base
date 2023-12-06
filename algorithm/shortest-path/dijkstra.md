- https://oi-wiki.org/graph/shortest-path/#dijkstra-%E7%AE%97%E6%B3%95
```python
def dijkstra(e,s):
  '''
  输入：
  e:邻接表
  s:起点
  返回：
  dis:从s到每个顶点的最短路长度
  '''
  dis = defaultdict(lambda:float("inf"))
  dis[s] = 0
  q = [(0,s)]
  vis = set()
  while q:
      _, u = heapq.heappop(q)
      if u in vis:
          continue
      vis.add(u)
      for v,w in e[u]:
          if dis[v] > dis[u] + w:
              dis[v] = dis[u] + w
              heapq.heappush(q,(dis[v],v))
  return dis
```
- 参考
  - [[heapq]]
  - [[adapter#priority_queue]]
- [[greedy]]地每次找到离单源最近
  - 比较[[dp]]的[[bellman-ford]]和[[floyd]]
  - 这里拆分的“子问题”（一个点到另一个点）是可以贪心的
  - 那里的“子问题”（有限条边/有限个点最短路）是需要[[dp]]的
    - 即[[re-classification]]
- 用[[adapter#priority_queue]]维护其它点到出发点的距离
  - 不是“到前沿的距离”！！
  - 对比[[minimum-spanning-tree]]中的prim
- 证明：[[induction]]，每一步都保证最优
  - 你填进一个点时，如果经由其它点到达，只会更差
  - 这里用到了无负权
  - 对比[[minimum-spanning-tree]]中的prim算法，这里的本质比较是
    - 源点到当前点最优路径
    - 源点到其它点最优路径（比到当前点最优路径长）
    - 两者比较
    - 两者都不止是一条边
    - 所以不能整张图加某个数
    - 所以不能像[[minimum-spanning-tree]]prim一样简单地处理负权
- 关于“访问过”点集`vis`
  - 不需要专门维护“访问过”点集
  - 因为折返回去无负权，路不会更短，所以不满足条件，不进frontier
  - 但是可以提高效率
- 例子：从$(0,0)$到$(i,j)$最短路
  - 不需要[[graph/save]]存图，直接由规则知道每个点相邻的是哪些点
  - 每次循环中，选（堆中）最小的点（也就是单源最短路）考察，并按规则往frontier加其相邻点（具体地，相邻不越界且路径更优就加）