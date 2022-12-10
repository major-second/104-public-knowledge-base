- https://leetcode.com/problems/jump-game-ii
```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        int end = nums.size()-1;
        int current = 0;
        int jumpNum = 0;
        for (int prevMax = 0; prevMax < end; jumpNum++){
            int currentMax = prevMax;
            for (; current<=min(prevMax, end) ;current++){
                currentMax = max(currentMax, nums[current] + current);
            }
            prevMax = currentMax;
        }
        return jumpNum;
    }
};
```
- 属于贪心[[greedy]]，一直不回头走到黑即可
  - 反正，多走不会比少走差！
- 贪心中的“区间”思想
  - 和[[two-pointers]]有点像，就是不给出精确值，而是给出可能范围
  - [[two-pointers]]是一次排除一系列值，这个是一次可行一系列值
  - 也就是：不要精确地计算`dp[i][j]`否则显然超时。需要看一步最多到多少，两步最多到多少……
  - 注意[[algorithm/special-case]]：长度为1，输出为0