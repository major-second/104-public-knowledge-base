# 核心
- 核心是递推，优中选优
  - 利用了之前已经计算过的东西
- 如果不需要选，那就是[[greedy]]
# 举例
- 最典型帮助理解的例子[[1388-pizza-with-3n-slices]]
  - 我们先不考虑首尾相接的问题，认为是“$3n$个元素中找$n$个两两不相邻使和最大”
    - 如果选最大的任意个元素，那就是[[greedy]]，不需要选，一股脑所有数放上即可
    - 如果选最大的任意个不相邻元素，那就是“01”型动态规划，存储两种可能（目前为止最后一个数选了/没选），每次从两种可能优中选优
    - 如果选最大的$n$个不相邻元素，那需要存储的状态更多，也就是之前最后一个数选了/没选，然后最多已经选取了多少个元素
      - 换句话说：你选了太多垃圾元素占“名额”不好
  - 这三种情况越来越不贪心，需要存储、优中选优的可能性越来越多
  - 参考[[general-principles/special-case]]思想，多次退化
- [[368-largest-divisible-subset]]
  - 讲到不能贪心，需要优中选优
# 注意
- 要注意递推选用哪个变量
比如https://leetcode.cn/contest/weekly-contest-286/problems/maximum-value-of-k-coins-from-piles/
需要选择堆编号
比如Floyd，选择“中转站”编号
- https://leetcode.cn/problems/longest-palindromic-substring/
如果普通动规，需要$n^2$
注：[[manacher]]只需要$O(n)$
- 注意选择方向
  - 例如[[10-regular-expression-matching]]，从后往前看
# 状态压缩
- 把不需要的扔掉，节省空间
  - [[10-regular-expression-matching]]
  - [[72-edit-distance]]
# 和其它联系
- 和[[oi-wiki-basic/recursion]]的关系：参考[[oi-wiki-basic/recursion]]
- 和[[induction]]往往有强联系
- 子问题相似性质，和[[self-similarity]]有强联系
- [[calculate-v]]中暴力计算
  - 即使不是暴力计算，整个强化学习中也充满了dp思想