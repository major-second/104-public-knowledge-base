抽象化：
```cpp
class Solution {
    void backtrack(vector<T>& ans_list, T& cur, param p){
        if (cur满足条件) {
            ans_list.push_back(cur);
            return;
        }
        if (cur可以尝试添加甲){
            cur.push_back(甲);
            backtrack(ans_list, cur, 添加甲后参数);
            cur.pop_back();
        }
        if (cur可以尝试添加乙){类似上面...}
    }
};
```
```cpp
class Solution {
    void backtrack(vector<string>& ans, string& cur, int open, int close, int n) {
        if (cur.size() == n * 2) {
            ans.push_back(cur);
            return;
        }
        if (open < n) {
            cur.push_back('(');
            backtrack(ans, cur, open + 1, close, n);
            cur.pop_back();
        }
        if (close < open) {
            cur.push_back(')');
            backtrack(ans, cur, open, close + 1, n);
            cur.pop_back();
        }
    }
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string current;
        backtrack(result, current, 0, 0, n);
        return result;
    }
};

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/
来源：力扣（LeetCode）
```