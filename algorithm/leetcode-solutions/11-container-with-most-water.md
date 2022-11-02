- https://leetcode.cn/problems/container-with-most-water/
- 前置：[[two-pointers]]
# 我的题解
```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int length = height.size();
        int lo = 0, hi = length-1;
        int maxArea = INT_MIN;

        while (lo<hi){
            int loValue = height[lo];
            int hiValue = height[hi];
            maxArea = max(maxArea, min(loValue, hiValue) * (hi-lo));
            if (loValue < hiValue){
                int loTmp = lo;
                while (height[loTmp]<=height[lo] && loTmp<hi) loTmp++;
                lo = loTmp;
            } else {
                int hiTmp = hi;
                while (height[hiTmp]<=height[hi] && hiTmp>lo) hiTmp--;
                hi = hiTmp;
            }
        }
        return maxArea;
    }
};
```