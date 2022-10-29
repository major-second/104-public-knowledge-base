- https://leetcode.com/problems/longest-valid-parentheses/
# [[stack]]解法（单调栈）
```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st;
        st.push(-1);
        int curMax = 0;
        int y = 0; // st: (-1, 0)
        for (int i=0; i<s.size(); i++){
            int deltaY = s[i]=='(' ? 1: -1;
            if (deltaY == 1){
                y++;
                st.push(i);
            } else {
                y--;
                st.pop();
                if (!st.empty()){
                    curMax = max(curMax, i - st.top());
                } else {
                    st.push(i);
                }
            }
        }
        return curMax;
    }
};
```
- 比如`((()())))((()(0))))`这个串
- 高度（纵坐标）从左从0开始，`(`加一`)`减一
  - 比如：刚刚考察第一个`(`时，栈中数据意义是`(-1, 0), (0, 1)`两个点
  - “减一”时，回忆单调栈性质，就应该弹出！
  - 注意始终保持栈非空！
- 考察到`0`（`14`号位）前，则`9, 10, 11, 13`四个点有价值
  - 它们的某种“高度”单调，为`0, 1, 2, 3`
  - 所以此时栈中数据意义是`(9, 0), (10, 1)`等四个点
- 本题特殊性：纵坐标每次值变化1，不会跳跃，所以栈中可以只有横坐标