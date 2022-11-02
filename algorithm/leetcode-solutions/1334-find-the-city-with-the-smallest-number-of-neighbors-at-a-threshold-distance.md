- https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
# [[shortest-path]] floyd算法
```cpp
class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        vector<vector<long long>> distance(n);
        for (int i=0; i<n; i++) {
            distance[i] = vector<long long>(n, INT_MAX);
            distance[i][i] = 0;
        }
        for (auto e: edges){
            int from = e[0];
            int to = e[1];
            int w = e[2];
            distance[from][to] = w;
            distance[to][from] = w;
        }

        for (int k=0; k<n; k++)
            for (int i=0; i<n; i++)
                for (int j=0; j<n; j++)
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]);

        int ansCity = 0;
        int cityCount = INT_MAX;
        for (int i=0; i<n; i++){
            int currentCityCount = 0;
            for (int j=0; j<n; j++){
                currentCityCount += distance[i][j] <= distanceThreshold;
            }
            if (currentCityCount<=cityCount){
                cityCount = currentCityCount;
                ansCity = i;
            }
        }
        return ansCity;
    }
};
```
- 这里没有做根据对称性的优化，但写起来简单
- 这里用了状态压缩
- 对于稠密图，用floyd挺好的