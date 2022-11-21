- https://leetcode.cn/problems/sliding-window-maximum/
```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        int length = nums.size();
        deque<pair<int, int>> q;
        for (int i=0; i<length; i++) {
            while(!q.empty() && q.back().first <= nums[i]) q.pop_back();
            q.push_back(make_pair(nums[i], i));
            if (i+1>=k) {
                if(q.front().second+k<=i) q.pop_front();
                ans.push_back(q.front().first);
            }
        }
        return ans;
    }
};
```
- [[deque]]
- [[sliding-window]]
- 其实本质还是单调栈，只不过要处理栈底出队列