- 前置[[poisson]]
  - 来自稀有事件、小数定律
    - 例子：盖革计数器，若半衰期远远长于考察的$t$，则考察时间内总物质的量近似不变
    - [[estimation]]
  - $t$时间内表示有多少个事件
  - non-decreasing step function
- 参考[[1-elements]]

[toc]
# 推导
## 一阶
- 计算泊松过程中一段时间内发生0个/1个事件概率
- 无记忆性
  - [[1-prob/independent]]
  - 因此$P_0(t+h)/P_0(t) = 1-p(h),\frac{P_0(t+h) - P_0(t)}{h} \to -常数\cdot P_0(t)$（当$h$小）
  - 其中$p(h)$表示泊松过程，$P_0$表示一段时间没有发生事件，常数来自$p(h)/h\to a$
- 列解微分方程得到
  - $p'_t = -at$
  - $P_0(t)=e^{-at}$（精确）
  - $P_1(h)=p(h)+o(h)=ah$（大约）
  - $\sum_{i=2}^m P_i(h)=o(h)$
## 高阶
- 类似刚才
  - $P_m(t+h)-P_m(t)=(我记为)\Delta P_m=ah(P_{m-1}-P_m)$
  - $P_m'=aP_{m-1}-aP_m,P_0=e^{-at}$
- 这是[[first-order-linear]]微分方程
  - 参考常数变易法思想进行换元
  - 而不是直接套公式！这里相当于[[leaky-abstraction]]
  - $Q_m=P_me^{at},Q'_m=aQ_{m-1}$
  - $Q_0=1,Q_1=x(常数为0由Q_m(0)=0,m=1,2,\cdots得到)$，等等
  - $Q_m=\frac{a^mt^m} {m!},P_m=\frac{a^mt^m} {m!}e^{-at}$
  - 这个$P_m$恰为参数为$at$的[[poisson]]分布，符合原始物理含义！
  - 除了时间，有时也用于空间分布
## 截面
- 参考[[symmetry#平移]]
- 给定时间发生事件个数：[[poisson]]，离散
- 给定事件需要多少时间：[[gamma-distribution]]
  - [[general-principles/special-case]]1个是[[gamma-distribution#指数分布]]
    - 参考[[可加性]]
  - 相邻等待时间：[[iid]] [[gamma-distribution#指数分布]]
    - 可能通过[[functional-equation]] $F(x+y)=F(y)+(1-F(y))F(x)$说明
    - 参考[[stationary-independent-increment]]
- 给定$t$时已经发生了$n$次，$X(t)=n$
  - [[conditional]]
  - $S_k$表示发生$k$次时花了多少时间
  - 则$P(S_i<s_i,\forall i)=F(s_1,\cdots,s_n)$
    - 其中$F$是[[order-statistics#multivariate]]的[[random-variable-functions#cdf]]
    - 和[[uniform-distribution]]相关
  - 证明：直接计算
- [[bernoulli-binom]]
  - $P(X(u)=k|X(t)=n)$
  - $P(X_1(t)=k|X_1(t)+X_2(t)=n)$
  - 本质都是[[symmetry#平移]], [[uniform-distribution]]原理
# 例题
- [[proportional#等车例题]]
## 曾经到过区间内
- 不停取数，每个数指数分布$f(x)=e^{-x}$，求和取到$x_0$就停，多大概率至少取到一次$[x_0,2]$之间（题目背景是我取到$x_0$，庄家小于$x_0$就不断取使得想比我大，但到2就爆仓）
 1. 指数分布求和其实是泊松过程，最后等效于$[x_0,2]$中何时至少有一个点
 2. 根据无后记忆性，$[x_0,2]$有点概率$1-e^{x_0-2}$
 3. 暴力[[self-similarity]]计算，就比较麻烦了，参考[[self-similarity]]
## 连续十次正
- 参考[[discrete-continuous]]
- [[success-runs]]计算出来连续十次硬币正面需要2046次
- 因此丢1000次，至少出现一次“连续十次正”概率估算
   - 整个过程相当于[[poisson-process]]
   - 第一次出现指定事件概率是[[gamma-distribution#指数分布]]
   - $2046$次中不出现概率是$1/e$
   - 因此$1000$中出现概率约等于$1-\frac 1{\sqrt e}$
## electrical pulses
- 来自[[a-first-course/0]]的简化
- pulses arrive according to a [[poisson-process]]，每次来时都+1
  - 这里是简化。原本是随机变量$X$
- decay exponentially
- 问题
  - 求[[characteristic-function]]
  - 简化问题：设考察1单位时间，$\alpha=1$
- 法一：[[characteristic-function]]的[[expectation#linearity]]
  - $\phi(t)=\sum_n \frac{\lambda^n e^{-\lambda}}{n!}[\int_0^1 exp(ite^{-s})ds]^n$
  - $=e^{-\lambda}\sum_n \frac{[]^n}{n!}=e^{\lambda(\int exp(ite^{-s})ds -1)}$
- 法二：[[discrete-continuous]]
  - 不是严格，是一个大致体会
  - [[bernoulli-binom]]
  - 分拆成$m$个独立发生的小时间段，$\phi(t)=\prod_k (\frac \lambda m exp(ie^{-k/m}t)+1-\frac \lambda m )$
  - $ln\phi(t)=\sum_k ln(1+\frac \lambda m (exp(ie^{-k/m}t)-1))\to \sum_k \frac \lambda m [exp(ie^{-k/m}t)-1]\to \lambda  \int_0^1 [exp(ite^{-s})-1] ds$
  - 注意，给定$t$，总能找到大的$m$，所以有“$\to$”。但是$t$可能很大，所以$exp(ite^{-k/m})-1$不能$\to ite^{-k/m}$