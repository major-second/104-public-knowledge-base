- [参考](https://en.wikipedia.org/wiki/Memoization)
  - 这是专有造出来的，不要写成memorization
- https://leetcode.cn/problems/can-i-win/submissions/
注意：不能傻傻地从`0b11111111`一点一点走到`0b00000000`这样，否则TLE
应该从0开始记忆化搜索。
这两者有啥区别？最坏复杂度一样，但是记忆化搜索有可能中途返回！所以这题和一般的dp不一样
- https://leetcode.cn/problems/generate-parentheses/
如果要递归，那么计算`n`对应结果时，提前记住之前所有结果当然很有帮助
注：观察：比如`n=3`，那么就是`()`中间插入2个`(`2个`)`，插入的时候，可能是“始终不侵犯最左侧`(`”，“第一对侵犯”，“第二对侵犯”，“两对都侵犯”4种可能。其中“始终不侵犯”就对应了`n=2`的2种答案。共5种答案
- 例子
  - [[486-predict-the-winner]]