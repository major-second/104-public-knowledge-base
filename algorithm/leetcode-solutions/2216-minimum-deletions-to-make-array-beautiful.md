- https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/
- [[greedy]]：一条路走到黑即可
  - 从前向后看，每次出现俩不同数时，它们留下，不留白不留
  - 你不留它们中的一个？那干嘛不删后面的呢
  - 这是[[greedy]]证明中常见的方法：回溯不会更优
- 注意这里用到[[DFA]]思想（两种状态：现在奇数或偶数）
- [[reduction]]减少代码复杂程度
  - 即：增大问题规模1，减少[[algorithm/special-case]]特判
```cpp
class Solution {
public:
    int minDeletion(vector<int>& nums) {
        int n = nums.size();
        if (n==1) return 1;
        nums.push_back(nums[n-1]); // unify the cases where there're odd number of elements after deletions.
        
        int prev = nums[0];
        bool currentEven = true;
        int totalDeletion = 0;
        for (int i=1;i<n+1;i++){
            if (currentEven && nums[i]==prev){
                totalDeletion++;
            } else {
                if (!currentEven) prev = nums[i];
                currentEven = !currentEven;
            }
        }
        return totalDeletion;
    }
};
```