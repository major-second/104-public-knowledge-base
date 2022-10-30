- https://leetcode.cn/problems/predict-the-winner/
- [[oi-wiki-basic/recursion]]
  - 这个记住已有状态，是[[记忆化搜索]]
- 注意[[sequence]]的初始化：`adv[i] = vector<int>(length+1);`这种初始预留空间
```cpp
class Solution {
public:
    int getAdv(vector<int>& nums, vector<vector<int>>& adv, int left, int right){ // inclusive
        if (adv[left][right]>INT_MIN) return adv[left][right];
        int leftAdv = nums[left] - getAdv(nums, adv, left+1, right);
        int rightAdv = nums[right] - getAdv(nums, adv, left, right-1);
        adv[left][right] = max(leftAdv, rightAdv);
        return adv[left][right];
    }
    bool PredictTheWinner(vector<int>& nums) {
        int length = nums.size();
        if (length<=2) return true;

        vector<vector<int>> adv(length);
        for (int i = 0; i < length-1; i++){
            adv[i] = vector<int>(length+1, INT_MIN);
            adv[i][i+1] = abs(nums[i] - nums[i+1]);
        }
        return getAdv(nums, adv, 0, length-1) >= 0;
    }
};
```
- 其实也可用[[dp]]
  - 甚至还能状态压缩！