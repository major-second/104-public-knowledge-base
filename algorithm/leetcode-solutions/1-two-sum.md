- https://leetcode.cn/problems/two-sum/
- 前置：[[sequence]]
# 暴力做法
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n; ++i){
            for (int j = i + 1; j < n; ++j){
                if (nums[i] + nums[j] == target){
                    return vector<int> {i, j};
                }
            }
        }
        return vector<int> {};
    }
};
```
- 可以看到
  - `.size()`的应用
    - 参考[[container-intro]]，是各种容器都有的函数
  - 列表初始化
  - 编译器会检查每个分支都必须`return`才能过，参考[[func]]
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
- [[two-pointers]]（时间不是最优因为需要排序）