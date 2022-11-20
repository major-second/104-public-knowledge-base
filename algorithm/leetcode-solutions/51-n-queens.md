- https://leetcode.cn/problems/n-queens/
- 前置[[backtrack]], [[oi-wiki-stl/string]]
```cpp
class Solution {
public:
    void backtrack(vector<vector<int>>& sols, vector<int>& currentState, const int n) {
        if (currentState.size()==n) {
            vector<int> stateCopy(currentState);
            sols.push_back(stateCopy);
            return;
        }
        for (int i = 1; i <= n; i++){
            bool valid = true;
            int currLength = currentState.size();
            for (int j = 0; j<currLength; j++){
                int diff = i - currentState[j];
                if (diff==0 || abs(diff)==currLength-j) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                currentState.push_back(i);
                backtrack(sols, currentState, n); 
                currentState.pop_back();
            }   
        }
    }

    vector<vector<string>> constructStringArrays(const vector<vector<int>>& sols, const int n){
        vector<vector<string>> answers;
        for (auto sol:sols){
            vector<string> answer;
            for (int i:sol){
                string row;
                row.insert(0, n, '.');
                row[i-1] = 'Q';
                answer.push_back(row);
            }
            answers.push_back(answer);
        }
        return answers;
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<vector<int>> sols;
        vector<int> currentState;
        backtrack(sols, currentState, n);
        vector<vector<string>> answers = constructStringArrays(sols, n);
        return answers;
    }
};
```