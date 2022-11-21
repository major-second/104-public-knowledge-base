- https://leetcode.cn/problems/redundant-connection-ii/
- 前置[[graph/save]], [[disjoint-set]]
- 注意[[algorithm/trivial-mistakes]]多解性
- 分类讨论！
  - 如果一个节点有两个父节点，则肯定去除其中一个
    - 注：本来你可以分类讨论
      - 如果有**有向**环，则去除成有向环的（对应着多余边是连自己祖先）
      - 否则去除靠后的（对应着多余边是连其它支或自己后代）
      - 然而[[disjoint-set]]不好区分是否有**有向**环
    - 所以对于存在“两个父节点”的，可以有一个傻办法
      - 去除一条边（由于多解性，必须去除靠后的边），看还是否归并到一个集合
      - 即假设法
  - 如果不存在一个节点有两个父节点，则直接去除成环的（对应多余边连根节点）
    - [[disjoint-set]]判断成环：$u\to v,且已经有find(v) == find(u)$
```cpp
class Solution {
public:
    int findSet(vector<int>& parents, int x){
        if (parents[x]==x) return x;
        parents[x] = findSet(parents, parents[x]);
        return parents[x];
    }
    void unionSet(vector<int>& parents, int x, int y){
        parents[findSet(parents, x)] = findSet(parents, y);
    }

    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> parents;
        for (int i = 0; i <= n; i++) parents.push_back(i);
        vector<int> directParent(n+1, -1);

        vector<int> firstCausedTwoParentsEdge;
        vector<int> lastCausedTwoParentsEdge;
        vector<int> lastCausedCycleEdge;
        for (auto e:edges) {
            int parent = e[0];
            int desc = e[1];
            if (findSet(parents, parent) == findSet(parents, desc)) lastCausedCycleEdge = e;
            if (directParent[desc] > 0) {
                lastCausedTwoParentsEdge = e;
                firstCausedTwoParentsEdge = vector<int>{directParent[desc], desc};
            }
            unionSet(parents, desc, parent);
            directParent[desc] = parent;
        }
        if (lastCausedTwoParentsEdge.empty()) return lastCausedCycleEdge;

        parents.clear();
        for (int i = 0; i <= n; i++) parents.push_back(i);
        for (auto e:edges) {
            int parent = e[0];
            int desc = e[1];
            if (parent != lastCausedTwoParentsEdge[0] || desc != lastCausedTwoParentsEdge[1])
            unionSet(parents, desc, parent);
        }

        for (int i=1; i<=n; i++) if (findSet(parents, i) != findSet(parents, 1)) return firstCausedTwoParentsEdge;
        return lastCausedTwoParentsEdge;
    }
};
```