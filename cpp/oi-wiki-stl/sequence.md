https://oiwiki.org/lang/csl/sequence-container/
## 序列式容器
好处
- 动态分配内存
- 重载比较和赋值运算符
- `=`初始化
- 列表初始化比如`vector<int> data {1, 2, 3};`

注意
- `[]`, `front()`, `back()`都是引用，`data()`指针，`begin()`迭代器
- `vector<bool>`会导致坑。可以换成`deque`等
- `back`表示末尾。如`push_back`. 对于`deque`也就有`push_front`

应用
https://leetcode-cn.com/problems/two-sum/
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int l = nums.size();
        for (int i = 0; i < l; ++i){
            for (int j = i + 1; j < l; ++j){
                if (nums[i] + nums[j] == target){
                    vector<int> r{i, j}; //列表初始化
                    return r;
                }
            }
        }
        vector<int> r{};
        return r;
    }
};
```
可以看到`.size()`的应用，列表初始化，以及编译器的检查（每个分支都必须`return`才能过）