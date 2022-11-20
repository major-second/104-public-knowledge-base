- https://leetcode.com/problems/longest-increasing-path-in-a-matrix
- [[graph/save]]提到过不需要额外存图
- 这是[[DAG]]
- 使用[[bfs]]
```cpp
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int numRows = matrix.size();
        int numCols = matrix[0].size();
        vector<vector<int>> numTilesFromMaxToCurr;
        for (int i = 0; i < numRows; i++) numTilesFromMaxToCurr.push_back(vector<int>(numCols, 0));

        queue<pair<int, int>> frontiers;
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                bool currIsLocalMaximum = true;
                vector<pair<int, int>> candidates {make_pair(i,j+1), make_pair(i,j-1), make_pair(i-1,j), make_pair(i+1,j)};
                for (pair<int, int> cand: candidates) {
                    if (cand.first < 0 || cand.second < 0 || cand.first >= numRows || cand.second >= numCols) continue;
                    if (matrix[cand.first][cand.second] > matrix[i][j]) {
                        currIsLocalMaximum = false;
                        break;
                    }
                }
                if (currIsLocalMaximum) frontiers.push(make_pair(i, j));
            }
        }

        int maxLength = 0;
        while (!frontiers.empty()) {
            pair<int, int> front = frontiers.front();
            int i = front.first;
            int j = front.second;
            vector<pair<int, int>> candidates {make_pair(i,j+1), make_pair(i,j-1), make_pair(i-1,j), make_pair(i+1,j)};
            for (pair<int, int> cand: candidates) {
                if (cand.first < 0 || cand.second < 0 || cand.first >= numRows || cand.second >= numCols) continue;
                if (matrix[cand.first][cand.second] < matrix[i][j]
                     && numTilesFromMaxToCurr[cand.first][cand.second] < numTilesFromMaxToCurr[i][j] + 1){
                         numTilesFromMaxToCurr[cand.first][cand.second] = numTilesFromMaxToCurr[i][j] + 1;
                         maxLength = max(maxLength, numTilesFromMaxToCurr[i][j] + 1);
                         frontiers.push(make_pair(cand.first, cand.second));
                     }
            }
            frontiers.pop();
        }
        return maxLength+1;
        
    }
};
```