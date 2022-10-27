- 前置[[container-intro]]
- [原文](https://oiwiki.org/lang/csl/associative-container/)
# 首要特点和典型操作
这个`set`和数学的`set`不同，有序（默认从小到大）。所以有
- `.erase(迭代器或迭代器区间)`
- `.erase(键)`
- `.lower_bound()`
  - 复杂度$O(logn)$
  - 返回迭代器[[iterator]]，可以`*`取值
  - 如果没有，返回`end()`
    - 对`end()`解引用的结果我们不去纠结
  - 对应：大于等于某值的最小元素，即“闭”
- `.upper_bound()`：大于等于改为大于，即“开”
  - 这里的`lower, upper`含义和数学中上下界不同
  - 具体地，他们都接近于某个集合的“下界”，但`upper`较大
- 高效的`.find()`查找值，返回迭代器（如果没有也是返回`end()`）
- `count(x)`看键为`x`元素数量
  - 不一定要求不能重键（你不能重键的集合也有看是否存在的需求啊）
  - 这说明`set<pair<>>`不能代替`map`
## 举例
```cpp
  set<int> s {1,2,3};
  s.insert(4);
  auto it = s.begin();
  auto it2 = it;
  it++; it++;
  s.erase(it2, it);
  for (int i:s) cout<<i<<endl;
  cout<<endl;
  for (int i=2;i<=6;i++) {
    auto itl = s.lower_bound(i);
    if (itl == s.end()) cout<<'e'<<endl; else cout<<*itl<<endl;
    auto itu = s.upper_bound(i);
    if (itu == s.end()) cout<<'e'<<endl; else cout<<*itu<<endl;
  }
```
- 结果：`34 33 34 4e ee ee`
## 重载比较
```cpp
struct cmp {
  bool operator()(int a, int b) { return a > b; }
};
set<int, cmp> s;
```
变为从大到小
## 其它注意
- `map`迭代器解引用是`pair<Key, T>`
  - 插入时可以插入`pair<Key, T>(...)`这种
  - 也可以通过下标插入`s[k] = v;`
- 删除
    - 用`erase(key)`删除会删除所有
    - `multimap`没法直接删除`pair`
      - 所以需要`erase(pos)`（迭代器），最灵活
    - 当然`set<pair<>>`，不同于`multimap`，可以直接删除`pair`
- 下标访问`map`，下标是本来没有的，就产生无意义新元素，降低效率
  - 所以`find()`很好
- 范围`for`
  - `(auto x:s)`
  - 或者`(auto& x:s)`（传引用）
  - `x`类型就是`<>`里面填的那个东西
## 无序关联式
参考[[hash-table]]
https://oiwiki.org/lang/csl/unordered-container/
- 里面讲到了哈希高级玩法（防hack）

codeforces hack你的哈希函数，有意思
- 利用哈希，平均情况下大多数操作常数复杂度
- 当然，填的类型必须[[hashable]]，比如`set`就不能往里填
  - 相比之下，有序的那些容器，只要能比较大小即可往里填
## 应用
- [原文](https://oiwiki.org/lang/csl/associative-container/)所说和[[greedy]]密切相关在后面例子里有
- 
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