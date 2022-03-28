- 前置[[intro]]

https://oiwiki.org/lang/csl/associative-container/
这个`set`和数学的`set`不同，有序（默认从小到大）。所以有
- `erase(pos)`（输入迭代器，不是输入整数）
- `lower_bound`（$O(logn)$）（如果没有，返回`end()`）（是大于等于）

- `map`迭代器解引用是`pair<Key, T>`
  - 插入时比较麻烦，需要插入`pair<Key, T>(...)`

无序的看个乐https://oiwiki.org/lang/csl/unordered-container/
不常用
codeforces hack你的哈希函数，有意思

## 应用
https://leetcode-cn.com/problems/two-sum/submissions/
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> mp;
        int l = nums.size();
        for (int i = 0; i < l; ++i){
            mp.insert(pair<int, int>(nums[i], i));
        }
        for (int i = 0; i < l; ++i){
            auto it = mp.find(target - nums[i]);
            if (it != mp.end()){
                if (i != it->second){
                    return vector<int> {i, it->second};
                }
            }
        }
        return vector<int> {};
    }
};
```
注意判断不能相等。
注意`->second`，`map`中的`pair`等等

## 有序集和`lower_bound`应用
https://leetcode-cn.com/problems/container-with-most-water/submissions/
```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = height.size();

        map<int, int> mp;
        int mono_max = height[0];
        mp.insert(pair<int, int>(height[0], 0));

        for (int i = 1; i < l; ++i){
            if (height[i] > mono_max){
                mono_max = height[i];
                mp.insert(pair<int, int>(height[i], i));
            }
        }

        map<int, int> rev_mp;
        int mono_rev_max = height[l - 1];
        rev_mp.insert(pair<int, int>(height[l - 1], l - 1));

        for (int i = l - 1; i >= 0; --i){
            if (height[i] > mono_rev_max){
                mono_rev_max = height[i];
                rev_mp.insert(pair<int, int>(height[i], i));
            }
        }

        /*
        for (auto it = mp.begin(); it != mp.end(); it++){
            cout<<it->second<<endl;
        }

        for (auto it = rev_mp.begin(); it != rev_mp.end(); it++){
            cout<<it->second<<endl;
        }
        */

        int res = 0;
        for (auto it = mp.begin(); it != mp.end(); it++){
            int left_h = it->first;
            //cout<<left_h;
            int left_pos = it->second;
            //cout<<left_pos;
            auto right_it = rev_mp.lower_bound(left_h);
            if (right_it != rev_mp.end()){
                int right_pos = right_it->second;
                int tmp_res = (right_pos - left_pos) * left_h;
                res = tmp_res > res ? tmp_res : res;
            }
        }
        for (auto it = rev_mp.begin(); it != rev_mp.end(); it++){
            int right_h = it->first;
            //cout<<right_h;
            int right_pos = it->second;
            //cout<<right_pos;
            auto left_it = mp.lower_bound(right_h);
            if (left_it != mp.end()){
                int left_pos = left_it->second;
                int tmp_res = (right_pos - left_pos) * right_h;
                res = tmp_res > res ? tmp_res : res;
            }
        }
        return res;
    }
};
```