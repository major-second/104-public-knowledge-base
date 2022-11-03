- https://leetcode.cn/problems/rotate-array/
- 法一[[oi-wiki-basic/simulate]]需要额外空间
- 法二三次翻转（可以使用[[algorithm]]的`reverse`）
```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin()+k);
        reverse(nums.begin()+k, nums.end());
    }
};
```
- 法三：也是[[oi-wiki-basic/simulate]]，但是是结果导向：直接看“谁最后到1号位，然后它的位又被谁占了”以此类推