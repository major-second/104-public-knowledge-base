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
```cpp
int solution(vector<int> &A) {
    A.push_back(0);
    int length = A.size();
    for (int i=0; i<length; i++){
        int curr_value = A[i];
        int curr_index = i;
        while (0 <= curr_value && curr_value <= length){
            curr_index = curr_value;
            curr_value = A[curr_index];
            A[curr_index] = 9999999; // A[0] = 9999999 for 0 exists
        }
    }
    for (int i=0; i<length; i++){
        if (A[i] != 9999999) return i;
    }
    return length;
}
```
这个不是在[[leetcode-solutions/0-metadata]]上做的，格式有点不同