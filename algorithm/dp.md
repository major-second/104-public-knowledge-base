核心是递推，优中选优（利用了之前已经计算过的东西）
如果不需要选，那就是[[greedy]]
- 举例：[[7-logical-agents]]，[[9-inference-in-FOL]]的forward
- 要注意递推选用哪个变量
比如https://leetcode-cn.com/contest/weekly-contest-286/problems/maximum-value-of-k-coins-from-piles/
需要选择堆编号
比如Floyd，选择“中转站”编号
- https://leetcode-cn.com/problems/longest-palindromic-substring/
如果普通动规，需要$n^2$
注：[[manacher]]只需要$O(n)$
- https://leetcode-cn.com/problems/regular-expression-matching/submissions/
注意方向：从前往后（已知前，递推后）
具体地：如果最后一位不是`*`，那么各退一步。否则要不然`p`退`a*`两个字符，要不然`s`退`a`一个字符
注：其实也可以说是[[记忆化搜索]]