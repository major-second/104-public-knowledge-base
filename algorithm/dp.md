核心是递推，优中选优
如果不需要选，那就是[[greedy]]
- 要注意递推选用哪个变量
比如https://leetcode-cn.com/contest/weekly-contest-286/problems/maximum-value-of-k-coins-from-piles/
需要选择堆编号
比如Floyd，选择“中转站”编号
- https://leetcode-cn.com/problems/longest-palindromic-substring/
如果普通动规，需要$n^2$
注：[[manacher]]只需要$O(n)$