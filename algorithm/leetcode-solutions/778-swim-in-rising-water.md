- https://leetcode.cn/problems/swim-in-rising-water/description/
- [[disjoint-set]]
- [[hash]]（由水深查位置）
- 联系[[graph/save]]中讲到的“相邻块”，参考[[329-longest-increasing-path-in-a-matrix]]
```cpp
class Solution {
public:
    pair<int, int> findSet(vector<vector<pair<int, int>>>& parents, pair<int, int> x){
        if (x.first == parents[x.first][x.second].first && x.second == parents[x.first][x.second].second) return x;
        parents[x.first][x.second] = findSet(parents, parents[x.first][x.second]);
        return parents[x.first][x.second];
    }
    void unionSet(vector<vector<pair<int, int>>>& parents, pair<int, int> x, pair<int, int> y){
        pair<int, int> xIndex = findSet(parents, x);
        parents[xIndex.first][xIndex.second] = findSet(parents, y);
    }

    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        int total = n * n;
        vector<pair<int, int>> depth2location(n*n+1, make_pair(0, 0));
        for (int i=0; i<n; i++) for (int j=0; j<n; j++) {
            int depth = grid[i][j];
            depth2location[depth] = make_pair(i, j);
        }

        vector<vector<pair<int, int>>> parents;
        for (int i=0; i<n; i++) {
            vector<pair<int, int>> row;
            for (int j=0; j<n; j++) {
                row.push_back(make_pair(i, j));
            }
            parents.push_back(row);
        }

        for (int d=0; ;d++){
            pair<int, int> currLocation = depth2location[d];
            int curX = currLocation.first;
            int curY = currLocation.second;
            vector<pair<int, int>> cands{make_pair(curX-1, curY), make_pair(curX, curY-1),
                                         make_pair(curX+1, curY), make_pair(curX, curY+1)};
            for (auto cand:cands) {
                if (cand.first < 0 || cand.first >= n) continue;
                if (cand.second < 0|| cand.second>= n) continue;
                if (grid[cand.first][cand.second] < d) unionSet(parents, currLocation, cand);
            }
            if (findSet(parents, make_pair(0, 0)) == findSet(parents, make_pair(n-1, n-1))) return d;
        }
        return -1;
    }
};
```
- 其他方法
  - [[binary-search]]二分答案，结合[[bfs]], [[dfs]]