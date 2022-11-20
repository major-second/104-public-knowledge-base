- 法一[[hash]]
```cpp
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int length = nums.size();
        for (int& n:nums) if (n <= 0) n = length + 1;
        for (const int n:nums) {
            int absn = abs(n);
            if (1 <= absn && absn <= length && nums[absn-1] > 0) nums[absn - 1] *= -1;
        }
        for (int i = 0; i < length; i++) if (nums[i] > 0) return i+1;
        return length+1;
    }
};
```
- 法二：换位，仍能保证[[inplace]]操作