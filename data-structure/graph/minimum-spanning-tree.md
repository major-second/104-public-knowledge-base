- https://oi-wiki.org/graph/mst/
- kruskal：参考[[greedy]]，拟阵思想
  - 每次取能连两部分的最小边
  - 需要先排序
  - 需要[[disjoint-set]]维护连通性
  - $O(eloge)$，边很多时慢
  - 不怕负数
- prim
  - 参考[[greedy]]
  - 参考[[shortest-path]]的dijkstra算法
    - 维护前沿，每次找离当前前沿最近的点
    - 比较dijkstra是维护离源最近！
  - 需要[[adapter]]优先队列维护
    - 也可以用二叉堆（相比优先队列，可以删除之前不需要的元素，更快）
    - 这点和[[shortest-path]]中的dijkstra一样
  - 边很多稠密时比kruskal快，例如[[1584-min-cost-to-connect-all-points]]
  - 证明：反证[[proof-by-contradiction]]
    - 贪心A和最优B，第一个“出岔子”的边，把最小生成树分成两个联通分量
    - 这两个连通分量由一条边联系，那反正一条边，干嘛不取最小？
- 以上最小生成树算法不怕负数
  - 为什么[[shortest-path]]的dijkstra算法怕，而这里类似原理的prim不怕？
  - 首先这两个维护的不一样！这个是前沿，那个是源
  - “局部性”不同
    - dijkstra反证证明中，你如果不是从当前路径到某个点，可以绕一圈。绕一圈中如果有负权，就会造成麻烦
      - 一条边，对一圈的很多边，所以你也不能整个图权整体加一个数
    - 这里反证证明中，每次一条边比较一条边！
      - 而且因此你也可以整个图加一个数