- 前置[[markov-process]]
- 参考[[5-markov-chain]]（实际问题求概率等很好用）
# 定义
- state space为可数（一般记为$0,1,\cdots$）的[[markov-process]]
  - 所以有$P_{ij}^{n,n+1},P_{ij}$等记号
  - 一般情况转移矩阵和$n$有关，我们先考察无关的（stationary transitional probabilities
    - 注意区分于[[stationary-processes]]
- $P(X_{t+1}|\cdots, X_{t-1},X_t) = P(X_{t+1}|X_t)$
- 一个具体实例所需要的：初始时分布和状态转移矩阵$P$
  - 行向量（转移前分布）乘以矩阵等于行向量（转移后分布）
  - 分布，自然加和为1，各自非负
  - 矩阵每行也同理
  - 为何说确定初始分布和转移矩阵就确定过程？只需证明任意realization的概率都可由此计算
# 实例
## SPATIALLY HOMOGENEOUS
- 和[[iid]]离散随机变量相关
- 转移矩阵每行都相同，为$a_0,\cdots,a_n,\cdots$
- 所以这个是[[stationary-processes]]
## 