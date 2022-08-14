- 定义：$P(X_{t+1}|\cdots, X_{t-1},X_t) = P(X_{t+1}|X_t)$
- 一个具体实例所需要的：初始时分布和状态转移矩阵$P$
- 满足一定条件时，转移矩阵$P$的$n$次幂到一定迭代次数后收敛不变
  - 且形如$$\left(\begin{matrix}\pi(1)&\pi(2)\\\pi(1)&\pi(2)\end{matrix}\right)$$
  - 其中$\sum \pi(i)=1$
  - $\pi P=\pi, PP=P$显然
- “一定条件”
  - 非周期：即$\{n|n\ge 1, P_{ii}^n>0\}$集合不能全是某整数倍数
  - 连通
  - 状态数可以有限/无限
  - $\pi$称为平稳分布
- 因此实际采样过程
  - 初始一个分布（如高斯）
  - 转移$n_1$次，开始采样
  - 再转移$n_2$次，这样得到了$n_2$组样本
- 细致平稳条件：$\pi_i P_{ij} = \pi_j P_{ji} \Rightarrow \sum_i \pi_i P_{ij} = \sum_i \pi_j P_{ji}=\pi_j\sum_i P_{ji}=\pi_j\Rightarrow \pi P=\pi$，是一个找到$P$的充分条件