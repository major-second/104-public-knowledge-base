- 前置
  - [[4-probability]]
  - [[random-variable-introduction]]
# 2 Two Simple Examples of Stochastic Processes
- 定义：每个$t$，对应一个随机变量$X_t$或称$X(t)$
  - $t$可能是离散时间${0,1,\cdots}$，连续$[0,\infty)$，乃至多维等
  - 关键词：独立性[[1-prob/independent]]，重复试验
  - 指标集中任取有限个可得联合分布。这些分布是核心！
    - 联想：无穷维线性空间中线性无关的定义：任取有限个，无关
- [[brownian-motion]]
- [[poisson-process]]
# 3 Classification of General Stochastic Processes
- State Space
  - $\mathbb N$:discrete
  - $\mathbb R$: real-valued
  - $\mathbb R^k$: $k$-vector process
  - 注意这个是每个时刻$t$的取值范围，不是index
- index parameter set
  - 离散时间（$X_n$，可能参考[[random-walk]]）
  - 连续时间
  - 多维（[[poisson-process]]）
  - 区别于state space
  - [[poisson-process]]典型：discrete state space, continuous index parameter
- [[stationary-independent-increment]]
- martingale, 参考[[5-martingale-and-random-walk]]
  - [[brownian-motion]]显然是
  - 来源：iid随机变量相加[[random-walk]]
  - 均值为0的[[stationary-independent-increment]]
- [[markov-process]]
- [[stationary-processes]]
- renewal processes
  - 例如[[poisson-process]]可以理解成$\lambda$为参数指数分布的renewal counting process
  - 无需刻意区分renewal counting process/renewal process
- point processes
  - [[poisson-process]]换个角度，把index set变成集族（子集的集合），那就是poisson point process
  - state space还是不变