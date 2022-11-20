- https://leetcode.cn/problems/number-of-visible-people-in-a-queue/description/
- [[stack]]中单调栈
```cpp
class Solution {
public:
    vector<int> canSeePersonsCount(vector<int>& heights) {
        int n = heights.size();
        vector<int> ans(n, 0);
        stack<int> rightContour;
        for (int i = n-1; i>=0; i--){
            while(!rightContour.empty()){
                ans[i]++;
                if (rightContour.top() <= heights[i]) rightContour.pop();
                else break;
            }
            rightContour.push(heights[i]);
        }
        return ans;
    }
};
```