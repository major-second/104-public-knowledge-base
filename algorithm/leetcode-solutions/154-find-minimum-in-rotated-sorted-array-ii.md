- https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
```cpp
class Solution {
public:
    int findMinLR(const vector<int>& nums, int left, int right){
        // including right
        if (right-left+1<=2) return min(nums[left], nums[right]);
        const int mid = (left+right)/2;
        
        if (nums[left]>nums[mid]) return findMinLR(nums, left, mid);
        if (nums[mid]>nums[right]) return findMinLR(nums, mid+1, right);
        
        int lMin = findMinLR(nums, left, mid);
        if (lMin<nums[left]) return lMin;
        int rMin = findMinLR(nums, mid, right);
        return min(lMin, rMin);
        
    }
    int findMin(vector<int>& nums) {
        return findMinLR(nums, 0, nums.size()-1);
    }
};
```
- 这是[[divide-and-conquer]]，但是不知道分成几个问题（可能1个可能2个）
- 尽量多使得是一个！才能最快