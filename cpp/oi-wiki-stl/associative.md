- 前置[[container-intro]]
- [原文](https://oiwiki.org/lang/csl/associative-container/)
- 这个`set`和数学的`set`不同，有序（默认从小到大）。所以有
  - `erase(pos)`（输入迭代器，不是输入整数）
  - `.lower_bound`（$O(logn)$）（如果没有，返回`end()`）（是大于等于）
  - 高效的`.find()`查找值
  - 重载比较snippet:
```cpp
struct cmp {
  bool operator()(int a, int b) { return a > b; }
};

set<int, cmp> s;
```

其它注意
- `count`看有无（这说明`set<pair<>>`不能代替`map`）
- `map`迭代器解引用是`pair<Key, T>`
  - 插入时可以插入`pair<Key, T>(...)`
  - 也可以通过下标插入
  - `multimap`删除
    - `multimap`没法直接删除`pair`. 需要`erase(pos)`
    - `erase(pos)`（用迭代器）很有用，因为用`key`删除会删除所有
    - 当然，有时可以改用`set<pair<>>`，那就可以直接删除。但不是所有时候`set<pair<>>`都能代替`multimap`
- 下标访问可能引入无意义新元素。所以`find()`很好
- 范围`for`：`(auto x:s)`，或者`(auto& x:s)`（传引用），`x`类型就是`<>`里面填的那个。

无序的https://oiwiki.org/lang/csl/unordered-container/
- 里面讲到了哈希高级玩法（防hack）
codeforces hack你的哈希函数，有意思
- 利用哈希，平均情况下大多数操作常数复杂度
- 当然，填的类型必须hashable，比如`set`就不能往里填。相比之下，有序的那些容器，只要能比较大小即可。
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
注意要判断脚标不能相等。
注意`->second`，`map`中的`pair`等等

https://leetcode-cn.com/problems/4sum/submissions/
这题如果参考刚刚的“两数之和”用哈希的做法：注意题目要求！需要的数据结构是`set<multiset<int>>`，内层先`set`检脚标重复，然后造一个`multiset`，再塞进外层`set`.
当然，这其实是个假的哈希，因为用的是有序的（无序的没法往`<>`里填）……直接这么做搞不好反而会超时。
## 有序集和`lower_bound`应用
### 例1
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
### 例2
- 两组点A和B，若B中的点的$x,y$坐标都比A中某个点大，就称为支配。给定两组点，求最多多少支配对
- 当然[[hungarian]]可以做，但是复杂度太高
- [[greedy]]思想方法
  - 对于B中$x$最小的点，看能被它支配的A中点中，$y$最大的点
  - 简单思考原因
    - 一方面，$x$大了小了都没用，反正现在被支配，以后都被支配，所以就应该考察$y$大
    - 另一方面，现在这一对送上门不要白不要
- 所以应该先各自排序，然后随着考察B中点的$x$坐标变大，也就不断地把更多A中的点加到平衡树（`set`）中