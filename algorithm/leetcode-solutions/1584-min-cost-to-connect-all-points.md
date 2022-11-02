- https://leetcode.cn/problems/min-cost-to-connect-all-points/
- kruskal算法，[[greedy]]从小到大找边，需要[[disjoint-set]]
```cpp
class Solution {
public:
    int dist(const vector<int> a, const vector<int> b){
        int xDiff = abs(a[0] - b[0]);
        int yDiff = abs(a[1] - b[1]);
        return xDiff + yDiff;
    }

    int findSet(vector<int>& parents, const int x){
        if (x!=parents[x]) parents[x] = findSet(parents, parents[x]);
        return parents[x];
    }

    void UnionSet(vector<int>& parents, const int x, const int y){
        parents[findSet(parents, x)] = findSet(parents, y);
    }

    int minCostConnectPoints(vector<vector<int>>& points) {
        priority_queue<pair<int, pair<int, int>>> pq;

        int numPoints = points.size();
        vector<int> parents(numPoints);
        for (int i=0; i<numPoints; i++){
            for (int j=i+1; j<numPoints; j++){
                vector<int> point1 = points[i];
                vector<int> point2 = points[j];
                int distance = dist(point1, point2);
                pq.push(make_pair(-distance, make_pair(i, j)));
            }
            parents[i] = i;
        }
        
        int ans = 0;
        int edgeNum = numPoints - 1;
        while (edgeNum) {
            auto p = pq.top();
            int point1 = p.second.first;
            int point2 = p.second.second;
            if (findSet(parents, point1) != findSet(parents, point2)) {
                ans -= p.first;
                edgeNum--;
                UnionSet(parents, point1, point2);
            }
            pq.pop();
        }
        return ans;
    }
};
```
- 结构清晰，思路简单，不过效率不高
  - early stop：到边数了就可以停