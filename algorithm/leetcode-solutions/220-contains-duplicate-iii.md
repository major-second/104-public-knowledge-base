- https://leetcode.cn/problems/contains-duplicate-iii
# [[associative]]有序集合做法
```cpp
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        int currentCount = 0;
        int length = nums.size();
        multiset<int> window;
        multiset<int> negWindow;
        for (int i=0; i<length; i++) {
            if (currentCount == indexDiff+1) {
                int count = window.count(nums[i-indexDiff-1]);
                window.erase(nums[i-indexDiff-1]);
                negWindow.erase(-nums[i-indexDiff-1]);
                for (int j=0; j<count-1;j++){
                    window.insert(nums[i-indexDiff-1]);
                    negWindow.insert(-nums[i-indexDiff-1]);
                }
            } else{
                currentCount++;
            }

            long current = nums[i];
            auto upperIt = window.lower_bound(current);
            if (upperIt != window.end() && *upperIt - current <= valueDiff) return true;
            auto lowerIt = negWindow.lower_bound(-current);
            if (lowerIt != negWindow.end() && current - -*lowerIt <= valueDiff) return true;
    
            window.insert(nums[i]);
            negWindow.insert(-nums[i]);
        }
        return false;
    }
};
```
- 注意讨论[[iterator]]是`end()`（也就是没找到元素）情况
- 注意[[sliding-window]]防重措施
  - 每次看以一个位置结尾的所有二元组
  - 因此每次先考察前面集合，再插入自己
  - 注意可能有重复元素，需要`multiset`
- 注意要考虑滑窗大于数列长的情况！[[counter-examples]]