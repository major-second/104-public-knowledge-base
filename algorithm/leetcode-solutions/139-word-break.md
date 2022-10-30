- https://leetcode.com/problems/word-break/
# 我的题解
```cpp
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet;
        for (string word:wordDict) wordSet.insert(word);
        
        int n = s.size();
        vector<int> valid(n+1, 0);
        unordered_set<int> validIndices {0};
        valid[0] = 1; // empty string        
        
        for (int i=1; i<=n; i++){
            for (int index: validIndices){
                string cand = s.substr(index, i-index);
                valid[i] += (bool)wordSet.count(cand);
            }
            if (valid[i]) validIndices.insert(i);
        }
        return (bool)valid[n];
    }
};
```
- 注意可以使用[[associative]]中的无序集合
- 总体思想是递推，可参考联系[[dp]]，[[记忆化搜索]]等
- 也可以用[[bfs]], [[dfs]]等