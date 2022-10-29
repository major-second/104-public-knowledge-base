- https://oiwiki.org/basic/greedy/
# 概述
- 逻辑上，可以和[[oi-wiki/recursion]]，[[induction]]做联系，也就是对$n$, 考察规模$n-1$的问题
  - 刚刚提到[[induction]]，所以其证明很多时候也是[[induction]]
    - 另一种常见证明方法：反证
  - 注意需要具有“最优子问题”性质
- 和[[dp]]区别：不能反悔（回溯），一条路走下去
# 实例
- “区间”思想
  - [[45-jump-game-ii]]
- https://leetcode.cn/problems/minimum-deletions-to-make-array-beautiful/
这题贪心就行，碰到重复的，如果能不删就不删。证明自行脑补