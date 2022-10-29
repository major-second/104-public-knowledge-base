- https://leetcode.com/problems/generate-parentheses
```cpp
class Solution {
public:
    void backtrack(vector<string>& results, int n, string prefix, int openNum, int closeNum){
        if (openNum + closeNum == 2 * n) results.push_back(prefix);
        if (openNum < n) backtrack(results, n, prefix + '(', openNum+1, closeNum);
        if (openNum > closeNum) backtrack(results, n, prefix + ')', openNum, closeNum+1);
    }
    vector<string> generateParenthesis(int n) {
        vector<string> results;
        backtrack(results, n, "", 0, 0);
        return results;
    }
};
```
- [[backtrack]]