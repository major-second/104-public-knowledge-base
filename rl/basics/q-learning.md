- 前置：[[calculate-v]]
- [参考](https://zhuanlan.zhihu.com/p/110338833)
- 和[[calculate-v]]中的TD算法总体类似，即用[[self-similarity]], [[general-principles/recursion]]思想
- SARSA: $Q(S,A)$的更新目标是$R+\gamma Q(S',A')$，其中$S$产生$A$和$S'$产生$A'$是同一策略
  - 如果[[greedy]]策略，即总是取使$Q(S',A')$最大，那就是q-learning
  - epsilon-greedy：有一定概率不是贪心的结果，借此进行探索。随着时间推移可以调整比例
- q-learning: $Q(S,A)$的更新目标是$R+\gamma max_a Q(S',a)$
- 注：这里说的[[greedy]]策略的“层次”比一般算法题中[[greedy]]和[[dp]]的区别层次高
  - 你是不是觉得[[greedy]]是当前reward最高，[[dp]]是$Q$最高
  - 但实际上[[greedy]]是$Q$最高（其实已经考虑到[[dp]]的思想），而非贪心策略是有一定概率取其它动作进行探索，更新$Q$值等，使得最终找到更好的策略