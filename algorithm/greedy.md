- [跳跃游戏II](https://leetcode-cn.com/problems/jump-game-ii)
和[[双指针]]有点像，就是不给出精确值，而是给出可能范围。[[双指针]]是一次排除一系列值，这个是一次可行一系列值
不要精确地计算`dp[i][j]`否则显然超时。需要看一步最多到多少，两步最多到多少……
有一个坑：长度为1，输出为0
- https://leetcode-cn.com/problems/minimum-deletions-to-make-array-beautiful/
这题贪心就行，碰到重复的，如果能不删就不删。证明自行脑补