- https://leetcode.cn/problems/number-of-islands
# 粗糙的[[disjoint-set]]解法
```cpp
class Solution {
public:
    int findSet(vector<int>& parents, const int a){
        if (parents[a]!=a) parents[a] = findSet(parents, parents[a]);
        return parents[a];
    }
    void unionSet(vector<int>& parents, const int a, const int b){
        parents[findSet(parents, a)] = findSet(parents, b);
    }
    int numIslands(vector<vector<char>>& grid) {
        int numRows = grid.size();
        int numCols = grid[0].size();

        vector<int> parents(numRows * numCols, INT_MIN);

        for (int i=0;i<numRows;i++){
            for (int j=0;j<numCols;j++){
                if (grid[i][j] == '0') continue;
                parents[i * numCols + j] = i * numCols + j;
                if (i && grid[i-1][j] == '1') unionSet(parents, i * numCols + j, (i-1) * numCols + j);
                if (j && grid[i][j-1] == '1') unionSet(parents, i * numCols + j, i * numCols + (j-1));
            }
        }

        unordered_set<int> parentsSet;
        for (int i=0;i<numCols*numRows;i++) 
            if (parents[i] != INT_MIN) parentsSet.insert(findSet(parents, i));
        return parentsSet.size();
    }
};
```
- 此处没有路径压缩
- 注意[[special-case]]：全0全1是否通过
- 注意去重
- 注意`union`不能做函数名