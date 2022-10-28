核心是递推，优中选优（利用了之前已经计算过的东西）
如果不需要选，那就是[[greedy]]
- 举例：[[7-logical-agents]]，[[9-inference-in-FOL]]的forward
- 要注意递推选用哪个变量
比如https://leetcode.cn/contest/weekly-contest-286/problems/maximum-value-of-k-coins-from-piles/
需要选择堆编号
比如Floyd，选择“中转站”编号
- https://leetcode.cn/problems/longest-palindromic-substring/
如果普通动规，需要$n^2$
注：[[manacher]]只需要$O(n)$
# 状态压缩
- 把不需要的扔掉，节省空间
  - 例如[[10-regular-expression-matching]]
# 其它
- 和[[oi-wiki/recursion]]的关系：参考[[oi-wiki/recursion]]