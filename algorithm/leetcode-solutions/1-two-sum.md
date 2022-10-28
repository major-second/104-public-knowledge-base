- https://leetcode.cn/problems/two-sum/
# [[hash-table]]做法
- 参考[[associative]]
- 注意去重（参考[[algorithm/trivial-mistakes]]）
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        int n = nums.size();
        for (int i=0;i<n;i++) {
            if (mp.count(nums[i]) && nums[i] * 2 == target) return vector<int> {i, mp[nums[i]]};
            mp[nums[i]] = i;
        }
        for (int i=0;i<n;i++) {
            int remains = target - nums[i];
            if (mp.count(remains) && nums[i] * 2 != target) return vector<int> {i, mp[remains]};
        }
        return vector<int> {};
    }
};
```
# 其他做法
- 暴力
- [[双指针]]（时间不是最优因为需要排序）